from generico import Generico
from mysql.connector import Error


class Proveedores:
    def __init__(self):
        pass

    def registrar_proveedores(self,nombre_empresa,telefono):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        cur=None
        if db.conexion.is_connected(): # Validamos si la conexión con el servidor de MySQL (puerto 3306) 
            try:
              cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
              consulta="INSERT INTO proveedores(nombre_empresa,telefono) VALUES (%s,%s)"
              cur.execute(consulta,(nombre_empresa,telefono,))
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

    def listar_proveedores(self):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM proveedores")
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

    def buscar_por_telefono(self,telefono):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM proveedores WHERE telefono = %s",(telefono,))
                busqueda=cur.fetchone()

                if busqueda:
                    return busqueda 
                else:
                    return None
               
            except Exception as e:
                print(f"Error al buscar el telefono {e}")
                return None
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return None
    
    def buscar_por_id(self,id_proveedor):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM proveedores WHERE id_proveedor = %s",(id_proveedor,))
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



    def eliminar_proveedor(self,id_proveedor):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("DELETE FROM proveedores WHERE id_proveedor = %s",(id_proveedor,))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al eliminar el proveedor {e}")
                return False
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False
    
            
    def editar_proveedor(self,nombre_empresa,telefono,id_proveedor):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("UPDATE proveedores set nombre_empresa =%s, telefono =%s WHERE id_proveedor =%s",(nombre_empresa,telefono,id_proveedor))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al editar el proveedor {e}")
                return False
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False
               