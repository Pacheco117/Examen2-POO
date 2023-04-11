import mysql.connector

# Crea una conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="examen2"
)

# Crea un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Especifica la ruta completa del archivo .sql que deseas importar
ruta_archivo_sql = "C:/xampp/ruta/a/tu/archivo.sql"

# Lee el archivo .sql y almacena su contenido en una variable
with open(ruta_archivo_sql, "r") as archivo_sql:
    contenido_sql = archivo_sql.read()

# Ejecuta el contenido SQL para importar la base de datos
cursor.execute(contenido_sql)

# Confirma los cambios
conexion.commit()

# Cierra la conexión y el cursor
cursor.close()
conexion.close()

# Imprime un mensaje de confirmación
print("La base de datos se ha importado correctamente.")