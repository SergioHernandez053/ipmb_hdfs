import time
import mysql.connector
from pyhive import hive

# Configuración de Hive
HIVE_HOST = "hive-server"
HIVE_PORT = 10000
HIVE_DATABASE = "default"

# Configuración de MySQL
MYSQL_HOST = "mysql"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "hive_results"

# Guardar el último recuento de datos
last_count = 0

def check_hive_changes():
    """Verifica si hay cambios en Hive comparando el número total de registros."""
    global last_count
    try:
        # Conectar a Hive
        hive_conn = hive.Connection(host=HIVE_HOST, port=HIVE_PORT, database=HIVE_DATABASE)
        hive_cursor = hive_conn.cursor()

        # Obtener el número total de registros en la tabla "users"
        hive_cursor.execute("SELECT COUNT(*) FROM users")
        count = hive_cursor.fetchone()[0]

        hive_cursor.close()
        hive_conn.close()

        # Si hay un cambio en la cantidad de registros, devolvemos True
        if count > last_count:
            last_count = count
            return True
        return False

    except Exception as e:
        print(f"Error al verificar cambios en Hive: {e}")
        return False

def export_data():
    """Exporta los datos de Hive a MySQL si hay cambios."""
    try:
        # Conectar a Hive
        hive_conn = hive.Connection(host=HIVE_HOST, port=HIVE_PORT, database=HIVE_DATABASE)
        hive_cursor = hive_conn.cursor()
        
        # Obtener datos nuevos desde Hive
        hive_cursor.execute("SELECT country, COUNT(*) FROM users GROUP BY country ORDER BY COUNT(*) DESC LIMIT 10")
        data = hive_cursor.fetchall()

        if not data:
            print("No hay datos nuevos en Hive.")
            return
        
        # Conectar a MySQL
        mysql_conn = mysql.connector.connect(
            host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB
        )
        mysql_cursor = mysql_conn.cursor()

        # Limpiar la tabla antes de insertar nuevos datos
        mysql_cursor.execute("DELETE FROM summary")

        # Insertar nuevos datos en MySQL
        mysql_cursor.executemany("INSERT INTO summary (country, user_count) VALUES (%s, %s)", data)
        mysql_conn.commit()

        print(f"{len(data)} filas exportadas correctamente.")

        # Cerrar conexiones
        hive_cursor.close()
        hive_conn.close()
        mysql_cursor.close()
        mysql_conn.close()

    except Exception as e:
        print(f"Error en la exportación: {e}")

while True:
    if check_hive_changes():
        print("Se detectaron cambios en Hive. Exportando datos a MySQL...")
        export_data()
    else:
        print("No hay nuevos datos en Hive. Esperando...")
    
    time.sleep(10)  
