FROM apache/hadoop:3

WORKDIR /proyecto_hdfs_ipmb

COPY /hdfs_config/init_hdfs.sh init_hdfs.sh
USER root
RUN chmod +x init_hdfs.sh

CMD ["/bin/bash", "./init_hdfs.sh"]