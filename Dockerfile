FROM python:3.9

# Instalar dependencias
RUN pip install mysql-connector-python pyhdfs

# Copiar el script al contenedor
WORKDIR /app
COPY load_data.py /app/

CMD ["python", "load_data.py"]