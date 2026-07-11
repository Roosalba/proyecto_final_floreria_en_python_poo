from generico import Generico
from mysql.connector import Error
 

class Detalle_venta:
    def __init__(self):
        pass


    def agregar_detalle_venta(self,cantidad,sub_total,id_articulo,id_venta):
        db = Generico()
        cur=None
       
        if db.conexion.is_connected(): 
            try:
              cur= db.conexion.cursor()
              consulta="INSERT INTO detalle_ventas (cantidad,sub_total,id_articulo,id_venta) VALUES (%s,%s,%s,%s)"
              cur.execute(consulta,(cantidad,sub_total,id_articulo,id_venta,))

            # hacemos la consulta para descotar del stock
              cur.execute("UPDATE articulos SET stock = stock - %s WHERE id_articulo =%s",(cantidad,id_articulo))

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
    
    def listar_detalle_ventas(self):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM detalle_ventas")
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
    
    def buscar_detalle_ventas(self,id_detalle):
        db=Generico()
        cur=None
        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                cur.execute("SELECT * FROM detalle_ventas WHERE id_detalle = %s",(id_detalle,))
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
    

    def eliminar_detalle(self, id_detalle):
        db = Generico()
        cur = None
        
        if db.conexion.is_connected():
            try:
                cur = db.conexion.cursor()
                cur.execute("SELECT id_articulo, cantidad FROM detalle_ventas WHERE id_detalle=%s",(id_detalle,))
                resultado=cur.fetchone()
                # si el resultado viene vacio, significa que el usuario ingreso mal los datos
                if not resultado:
                    print("Error: El ID de detalle de venta no existe")
                    return False
                # Guardamos esos datos en variabes para usarlas en el siguiente
                id_articulo=resultado[0]
                cantidad_a_devolver=resultado[1]
                #hacemos la consulta para devolver lo que habia al stock

                cur.execute("UPDATE articulos SET stock = stock + %s WHERE id_articulo =%s",(cantidad_a_devolver,id_articulo))

                cur.execute("DELETE FROM detalle_ventas WHERE id_detalle = %s", (id_detalle,))
            
                # Confirmamos todas las operaciones juntas en la base de datos
                db.conexion.commit()
                return True
            except Exception as e:
            # Si algo falla en el medio (por ejemplo, se corta la luz tras el paso 2), 
            # el 'rollback' cancela todo para que el stock no quede mentiroso.
                print(f"Error al eliminar el detalle y restaurar stock: {e}")
                db.conexion.rollback() 
                return False
                
            finally:
                # Cerramos todo de manera prolija, tal como lo venías haciendo.
                if cur is not None:
                    cur.close()
                db.conexion.close()
                
        return False

    def editar_detalle(self,id_detalle,id_articulo_nuevo,id_venta_nueva, nueva_cantidad):
        db= Generico()
        cur=None

        if db.conexion.is_connected():
            try:
                cur=db.conexion.cursor()
                # 1.BUSCAR PARA SABER QUE HABIA ANTES, LO HACEMOS HACIENDO LA CONSULTA Y LUEGO GUARDAMOS EN LA VARIABLE RESULTADO
                cur.execute("SELECT id_articulo, cantidad FROM detalle_ventas WHERE id_detalle =%s",(id_detalle,))
                resultado_viejo=cur.fetchone()

                if not resultado_viejo:
                    print("Error: El ID de detalle no existe")
                    return False
                id_articulo_viejo= resultado_viejo[0]
                cantidad_vieja=resultado_viejo[1] #guardo la cantidad vieja

                # 2.BUSCO EL PRECIO DEL NUEVO ARTICULO(ASI CALCULO EL NUEVO SUBTOTAL)
                cur.execute("SELECT precio FROM articulos WHERE id_articulo =%s",(id_articulo_nuevo,))
                resultado_articulo = cur.fetchone()

                if not resultado_articulo:
                    print("Error: El nuevo ID articulo no existe")
                    return False
                precio_articulo = resultado_articulo[0]
                nuevo_sub_total = nueva_cantidad * precio_articulo

                # 3.DEVUELVO EL ARTICULO VIEJO AL STOCK "LAS FLORES"
                cur.execute("UPDATE articulos SET stock = stock + %s WHERE id_articulo =%s",(cantidad_vieja,id_articulo_viejo))


                # 4. ACTUALIZAMOS EL DETALLE(cambio todos los campo de la tabla)
                cur.execute("UPDATE detalle_ventas SET cantidad = %s, sub_total =%s, id_articulo=%s, id_venta=%s WHERE  id_detalle= %s",(nueva_cantidad,nuevo_sub_total,id_articulo_nuevo,id_venta_nueva,id_detalle))


                # 5.RESTO LAS NUEVAS FLOR DEL STOCK
                cur.execute("UPDATE articulos SET stock = stock - %s WHERE id_articulo = %s",(nueva_cantidad,id_articulo_nuevo))

                #confirmar los cambios
                db.conexion.commit()
                return True
            except Exception as e:
                print(f"Error al editar el detalle y ajustar stock: {e}")
                db.conexion.rollback() 
                return False
                    
            finally:
                if cur is not None:
                    cur.close()
                db.conexion.close()
                
        return False