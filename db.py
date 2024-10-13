import os
import psycopg2
from psycopg2 import OperationalError

# def get_db_connection():
#     conn = psycopg2.connect(
#         host="localhost",
#         port="5435",
#         database="sistema_matricula",
#         user="postgres",
#         password="admin123"
#     )
#     return conn


DATABASE_URL = os.getenv('DATABASE_URL')
def get_db_connection():
    try:
        # Conexión usando la URL de la base de datos
        conn = psycopg2.connect(DATABASE_URL)
        print("Conexión a PostgreSQL exitosa")
        return conn
    except OperationalError as e:
        print(f"La conexión a PostgreSQL falló: {e}")
        return None
