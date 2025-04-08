FROM python:3.9

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    libsasl2-dev \
    gcc \
    python3-dev \
    libffi-dev \
    && apt-get clean

RUN pip install pyhive thrift thrift_sasl sasl mysql-connector-python
RUN pip install pyhive[thrift]
RUN pip install impyla


# Copiar el script al contenedor
WORKDIR /app
COPY ./export_hive_mysql.py ./export_hive_mysql.py

# Ejecutar el script
CMD ["python3", "export_hive_mysql.py"]