FROM python:3.9

# Instalar dependencias
RUN pip install mysql-connector-python pyhdfs

# Copiar el script al contenedor
WORKDIR /app
COPY load_data.py /app/

CMD ["python", "load_data.py"]

ARG HIVE_VERSION
# Set HIVE_VERSION from arg if provided at build, env if provided at run, or default
# https://docs.docker.com/engine/reference/builder/#using-arg-variables
# https://docs.docker.com/engine/reference/builder/#environment-replacement
ENV HIVE_VERSION=${HIVE_VERSION:-3.1.3}

RUN apt-get update && apt-get install -y wget procps && \
	wget https://archive.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz && \
	tar -xzvf apache-hive-$HIVE_VERSION-bin.tar.gz && \
	mv apache-hive-$HIVE_VERSION-bin hive && \
	rm apache-hive-$HIVE_VERSION-bin.tar.gz && \
	apt-get --purge remove -y wget && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

ENV HIVE_HOME /opt/hive
ENV PATH $HIVE_HOME/bin:$PATH
ENV HADOOP_HOME /opt/hadoop-$HADOOP_VERSION


WORKDIR /opt