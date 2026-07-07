from generico import Generico
from mysql.connector import Error

class Cliente:
    def __init__(self):
       pass
    
    def agregar_clientes(self,id_cliente,nombre,telefono,email):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        cur=None
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
              cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
              consulta="INSERT INTO clientes(id_cliente,nombre,telefono,email) VALUES (%s,%s,%s,%s)"
              cur.execute(consulta,(id_cliente,nombre,telefono,email,))
              db.conexion.commit()

              return True
            except Exception as e:
                print(f"Error al registrar en la base de datos: {e}")
                return False
            finally:# es para que la conexion se cierre si o si
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False




    def listar_cliente(self):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
                cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
                cur.execute('SELECT * FROM clientes')
                resultado_cliente= cur.fetchall()
                return resultado_cliente
            
            except Error as e:
                print(f"No se pudo listar los clientes: {e}")
                return []# esto si no hay clientes me devuelve una lista vacia
            finally:
                cur.close()
                db.conexion.close()
        return[]
    

    def buscar_clientes(self,id_cliente):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM clientes WHERE id_cliente = %s",(id_cliente,))
                busqueda=cur.fetchone()

                if busqueda:
                    return busqueda 
                else:
                    return None
               
            except Exception as e:
                print(f"Error al buscar el ID {e}")
                return None
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return None
    

    def eliminar_cliente(self,id_cliente):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("DELETE FROM clientes WHERE id_cliente =%s",(id_cliente,))
                db.conexion.commit()
                filas_afectadas = cur.rowcount # sirve para contar las filas que fueron modificadas
                if filas_afectadas >0:
                    return True
                else:
                    return False
                
            except Exception as e:
                print(f"Error al eliminar {e}")
                return False
            finally:# es para cerrra la conexion
                if not None:# comprueba que el cursor realmente exista antes de cerrarlo
                    cur.close()
                db.conexion.close()
        return  False
    
    
    def editar_clientes(self,id_cliente,nombre,telefono,email):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("UPDATE clientes set nombre =%s, telefono=%s, email=%s WHERE id_cliente = %s",(nombre,telefono,email,id_cliente))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al Editar : {e}" )
                return False
        
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()

        return False