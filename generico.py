from mysql.connector import Error
import mysql.connector

class Generico():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host = 'localhost',
                port = 3307,
                user = 'root',
                password = '', 
                database='floreria'
            )

        except Error as error:
            print(f'No se pudo realizar la conexion con la base de datsos: {error}')
print("Conexion exitosa")