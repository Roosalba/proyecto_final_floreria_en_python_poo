from generico import Generico
from mysql.connector import Error

class Metodo_pago:
    def __init__(self):
        pass

    def registrar_metedo_pago(self,nombre_metodo):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
              cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
              consulta="INSERT INTO metodos_pago(nombre_metodo) VALUES (%s)"
              cur.execute(consulta,(nombre_metodo,))
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
    
    def listar_metodo_pago(self):
        db = Generico() 
        cur= None
        if db.conexion.is_connected():
            try:
               cur= db.conexion.cursor()
               cur.execute("SELECT * FROM  metodos_pago")
               resul_metedo_pago=  cur.fetchall()
               return resul_metedo_pago
                
            except Exception as e:
                print(f"Error al listar en la base de datos: {e}")
                return []
            finally:# es para que la conexion se cierre 
                if cur is not None: #cerramos el cursor si realmente se logro crear
                    cur.close()
                db.conexion.close()

        return[]


    def buscar_metodo_pago(self,id_metodo_pago):
        db= Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("SELECT * FROM metodos_pago WHERE id_metodo_pago = %s",(id_metodo_pago,))
                resul_metedo_pago = cur.fetchone()
                return resul_metedo_pago
            except Exception as e:
                print(f"Error al buscar el id del metodo de pago: {e}")
                return None
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return None
    


    def editar_metodo_pago(self,id_metodo_pago,nombre_metodo):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("UPDATE metodos_pago set nombre_metodo =%s WHERE id_metodo_pago = %s",(nombre_metodo,id_metodo_pago))
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
    
    def eliminar_metodo_pago(self,id_metodo_pago):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("DELETE FROM metodos_pago WHERE id_metodo_pago =%s",(id_metodo_pago,))
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
                if cur is not None:# comprueba que el cursor realmente exista antes de cerrarlo
                    cur.close()
                db.conexion.close()
        return  False
