from generico import Generico
from mysql.connector import Error

class Cliente:
    def __init__(self):
       pass

    def listar_cliente(self):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
                cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
                cur.execute('SELECT * FROM clientes')

                resultado_cliente= cur.fetchall()

            

                cur.close() #cerramos el cursor, es una buena practica
                return resultado_cliente
            
            except Error as e:
                print(f"No se pudo listar los clientes: {e}")
                return []# esto si no hay clientes me devuelve una lista vacia
        return[]