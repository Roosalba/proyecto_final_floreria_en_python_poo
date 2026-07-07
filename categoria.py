from generico import Generico
from mysql.connector import Error

class Categoria:
    def __init__(self):
        pass

    def registrar_categoria(self,nombre_categoria):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
              cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
              consulta="INSERT INTO categoria(nombre_categoria) VALUES (%s)"
              cur.execute(consulta,(nombre_categoria,))
              db.conexion.commit()

              return True
            except Exception as e:
                print(f"Error al registrar en la base de datos: {e}")
                return False
            finally:# es para que la conexion se cierre si o si
                cur.close()
                db.conexion.close()
        return False


    def listar_categoria(self):
        db = Generico() 
        cur= None
        if db.conexion.is_connected():
            try:
               cur= db.conexion.cursor()
               cur.execute("SELECT * FROM categoria")
               resul_categoria=  cur.fetchall()
               return resul_categoria
                
            except Exception as e:
                print(f"Error al listar en la base de datos: {e}")
                return []
            finally:# es para que la conexion se cierre 
                if cur is not None: #cerramos el cursor si realmente se logro crear
                    cur.close()
                db.conexion.close()

        return[]
    
    def buscar_categoria(self,id_categoria):
        db= Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("SELECT * FROM categoria WHERE id_categoria = %s",(id_categoria,))
                resul_categoria = cur.fetchone()
                return resul_categoria
            except Exception as e:
                print(f"Error al buscar el id de categoria: {e}")
                return None
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return None

    def editar_categoria(self,id_categoria,nombre_categoria):

        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("UPDATE categoria set nombre_categoria =%s WHERE id_categoria = %s",(nombre_categoria,id_categoria))
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
    
    def eliminar_categoria(self,id_categoria):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur= db.conexion.cursor()
                cur.execute("DELETE FROM categoria WHERE id_categoria =%s",(id_categoria,))
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

                