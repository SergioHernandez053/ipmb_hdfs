import mysql.connector
from pyhdfs import HdfsClient
import csv

# Configuración de HDFS
HDFS_HOST = "namenode"
HDFS_PORT = 50070
HDFS_FILE_PATH = "/user/hive/warehouse/summary.csv"

# Configuración de MySQL
MYSQL_HOST = "mysql"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "hive_results"

# Leer datos desde HDFS
client = HdfsClient(hosts=f"{HDFS_HOST}:{HDFS_PORT}")
with client.open(HDFS_FILE_PATH) as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

# Insertar datos en MySQL
conn = mysql.connector.connect(
    host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB
)
cursor = conn.cursor()
cursor.executemany("INSERT INTO summary (country, user_count) VALUES (%s, %s)", data)
conn.commit()
cursor.close()
conn.close()