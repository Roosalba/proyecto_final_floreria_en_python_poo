from generico import Generico
from mysql.connector import Error
from datetime import datetime

class Ventas:
    def __init__(self):
        pass


    def agregar_ventas(self,total,id_cliente,id_metodo_pago):
        db = Generico() # Este codigo inicializa la conexion a MySQL (host, puerto, usuario)
        cur=None
        fecha_automatica = datetime.now()#genero la fecha actual y hora actual automaticamente
        if db.conexion.is_connected(): # Validamos si la conexion con el servidor de MySQL (puerto 3306) 
            try:
              cur= db.conexion.cursor()#creamos el cursor,que es el objeto que nos permite enviar sentencias sql a la base de datos.
              consulta="INSERT INTO ventas(fecha,total,id_cliente,id_metodo_pago) VALUES (%s,%s,%s,%s)"
              cur.execute(consulta,(fecha_automatica,total,id_cliente,id_metodo_pago,))
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


    def listar_ventas(self):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM ventas")
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
    

    def buscar_venta(self,id_venta):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM ventas WHERE id_venta = %s",(id_venta,))
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
    

    def eliminar_venta(self,id_venta):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("DELETE FROM ventas WHERE id_venta = %s",(id_venta,))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al eliminar la venta {e}")
                return False
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False
    
    def editar_venta(self,id_venta,id_cliente,id_metodo_pago):
        db=Generico()
        cur=None
        fecha_automatica = datetime.now()#genero la fecha actual y hora actual automaticamente
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("UPDATE ventas set fecha =%s, id_cliente=%s, id_metodo_pago=%s WHERE id_venta =%s",(fecha_automatica,id_cliente,id_metodo_pago,id_venta))
                db.conexion.commit()
                filas_afectadas = cur.rowcount
                if filas_afectadas>0:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al editar la venta {e}")
                return False
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
        return False
    
   