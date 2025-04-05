FROM apache/hive:3.1.3

WORKDIR /proyecto_hdfs_ipmb
USER root

RUN apt-get update && apt-get install -y python3-pip 


RUN mkdir -p /home/hive/.beeline && chown hive:hive /home/hive/.beeline
USER hive

COPY hive/init.sql init_hive.sql
COPY userdata /app/userdata 

# ADD hive/hive-site.xml /opt/hive/conf/hive-site.xml

CMD [beeline -u jdbc:hive2://localhost:10000/ -f hive/init_hive.sql]