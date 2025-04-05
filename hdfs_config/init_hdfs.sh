#!/bin/bash
sleep 5
hdfs namenode


hdfs dfs -mkdir -p /user/hive/warehouse/userdata
hdfs dfs -chmod 777 /user/hive/warehouse/userdata  # Ajusta permisos
hdfs dfs -mkdir -p /user/hive/warehouse/metadata
hdfs dfs -chmod 777 /user/hive/warehouse/metadata

hdfs dfs -put /userdata/* /user/hive/warehouse/userdata/
hdfs dfs -put /metadata/* /user/hive/warehouse/metadata/