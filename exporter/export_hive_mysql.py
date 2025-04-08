import time
import mysql.connector
from pyhive import hive
import thrift
import thrift_sasl
from impala.dbapi import connect

# Configuración de Hive
HIVE_HOST = "hive-server"
HIVE_PORT = 10000
HIVE_DATABASE = "default"

# Configuración de MySQL
MYSQL_HOST = "mysql"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "hive_results"


def export_data():
    """Exporta los datos de Hive a MySQL si hay cambios."""
    try:
        # Conectar a Hive
        hive_conn = connect(host=HIVE_HOST, port=HIVE_PORT, auth_mechanism='PLAIN')
        hive_cursor = hive_conn.cursor()
        
        # Obtener datos nuevos desde Hive
        hive_cursor.execute("SELECT country, user_count FROM summary ORDER BY user_count DESC LIMIT 10")
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

export_data()

