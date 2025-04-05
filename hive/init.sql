CREATE EXTERNAL TABLE user
STORED AS AVRO
LOCATION '/user/hive/warehouse/userdata'
TBLPROPERTIES ('avro.schema.url'='user/hive/warehouse/metadata/userdata.avsc');

CREATE TABLE IF NOT EXISTS summary AS
SELECT country, COUNT(*) AS user_count
FROM usuarios
GROUP BY country
ORDER BY user_count DESC