from generico import Generico
from mysql.connector import Error

class Articulos:
    def __init__(self):
        pass

    def agregar_articulos(self,nombre,precio,stock,id_proveedor,id_categoria):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        cur=None
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
              cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
              consulta="INSERT INTO articulos(nombre,precio,stock,id_proveedor,id_categoria) VALUES (%s,%s,%s,%s,%s)"
              cur.execute(consulta,(nombre,precio,stock,id_proveedor,id_categoria))
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
    
    def listar_articulos(self):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM articulos")
                resultado= cur.fetchall()
                return resultado
            except Exception as e:
                print(f"Error al listar en la base de datos {e}")
                return[]
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()

        return []
    
    def buscar_articulos(self,id_articulo):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM articulos WHERE id_articulo = %s",(id_articulo,))
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
    

    def editar_articulos(self,id_articulo,nombre,precio,stock,id_proveedor,id_categoria):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("UPDATE articulos set nombre =%s, precio =%s, stock=%s, id_proveedor=%s, id_categoria=%s WHERE id_articulo =%s",(nombre,precio,stock,id_proveedor,id_categoria,id_articulo))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al editar el articulo {e}")
                return False
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False
    

    def eliminar_articulos(self,id_articulo):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("DELETE FROM articulos WHERE id_articulo = %s",(id_articulo,))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al eliminar articulos {e}")
                return False
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False
