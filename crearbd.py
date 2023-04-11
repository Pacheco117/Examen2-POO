import mysql.connector

# Crea una conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Crea un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Crea una nueva base de datos
cursor.execute("CREATE DATABASE examen2")

# Confirma los cambios
conexion.commit()

# Cierra la conexión y el cursor
cursor.close()
conexion.close()

# Imprime un mensaje de confirmación
print("La base de datos se ha creado correctamente.")