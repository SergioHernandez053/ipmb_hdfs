CREATE EXTERNAL TABLE userdata 
STORED AS AVRO 
LOCATION 'hdfs://namenode/user/hive/warehouse/userdata'
TBLPROPERTIES ('avro.schema.url'='hdfs://namenode/user/hive/warehouse/metadata/userdata.avsc');

CREATE TABLE IF NOT EXISTS summary AS
SELECT country, COUNT(*) AS user_count
FROM userdata
GROUP BY country
ORDER BY user_count DESC