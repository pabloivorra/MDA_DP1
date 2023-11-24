# Database connection functions
import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='192.168.1.212',
            user='eloy',
            password='eloyflexo',
            database='flexografico'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos MySQL: {e}")
        return None

def realizar_consulta(consulta):
    try:
        conexion = obtener_conexion()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            return resultados
    except Error as e:
        print(f"Error al realizar consulta: {e}")
    finally:
        if conexion is not None and conexion.is_connected():
            conexion.close()