#!/bin/bash
hdfs namenode


#hdfs dfs -mkdir -p hdfs://namenode/user/hive/warehouse/userdata
#hdfs dfs -chmod 777 hdfs://namenode/user/hive/warehouse/userdata  # Ajusta permisos
#hdfs dfs -mkdir -p hdfs://namenode/user/hive/warehouse/metadata
#hdfs dfs -chmod 777 hdfs://namenode/user/hive/warehouse/metadata

hdfs dfs -mkdir -p hdfs://namenode/user/hive/warehouse/userdata
hdfs dfs -chown hive hdfs://namenode/user/hive/warehouse/userdata  # Ajusta permisos
hdfs dfs -mkdir -p hdfs://namenode/user/hive/warehouse/metadata
hdfs dfs -chown hive hdfs://namenode/user/hive/warehouse/metadata

hdfs dfs -put /userdata/* hdfs://namenode/user/hive/warehouse/userdata/
hdfs dfs -put /metadata/* hdfs://namenode/user/hive/warehouse/metadata/