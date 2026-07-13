from generico import Generico
from mysql.connector import Error
 

class Detalle_venta:
    def __init__(self):
        pass


    def agregar_detalle_venta(self,cantidad,sub_total,id_articulo,id_venta):
        db = Generico()
        cur=None
        
        ''' hacemos la consulta para devolver lo que habia al stock, el campo %s se reemplaza despues por
            cantidad, no coloco la variable directamente por seguridad de inyeccion, en el rollback
            lo uso por si falla en insert o el update cancele la ejecucion, solo va a guardar los cambios
            si todas las consultas salen bien.
                       
            '''

       
        if db.conexion.is_connected(): 
            try:
              cur= db.conexion.cursor()

              cur.execute("SELECT stock FROM articulos WHERE id_articulo =%s",(id_articulo,))

              resu_stock = cur.fetchone()
              if not resu_stock or resu_stock[0]< cantidad:
                print("Error: El stock cambio o es insuficiente en la bases de datos. ")
                return
              
              # 1.  INSERTAR EL DETALLE
              consulta="INSERT INTO detalle_ventas (cantidad,sub_total,id_articulo,id_venta) VALUES (%s,%s,%s,%s)"
              cur.execute(consulta,(cantidad,sub_total,id_articulo,id_venta,))

            # hacemos la consulta para descotar del stock
              cur.execute("UPDATE articulos SET stock = stock - %s WHERE id_articulo =%s",(cantidad,id_articulo))

              db.conexion.commit()

              return True
            except Exception as e:
                print(f"Error al registrar en la base de datos: {e}")
                db.conexion.rollback() #  Si falla el UPDATE, deshace el INSERT
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
        
        '''
        para eliminar algun de detalle de venta hacemos lo siguiente:
        1. busco en detatalle venta que articulo era y que cantidad se iba a llevar usando el id_detalle
        2.Tomo esa cantidad que en este caso se llama, cantidad_a_devolver y se suma otra vez al stock del 
        articulo. (SET stock = stock + %s). El %s-> se reemplaza por la variable cantidad_a_devolver
        se hace asi para proteger los datos de las inyecciones.
        3.Una vez que el stock vuelve a su lugar, hacemos el delete para borrar el registro de detalle venta
        
        '''

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



                cur.execute("UPDATE articulos SET stock = stock + %s WHERE id_articulo =%s",(cantidad_a_devolver,id_articulo))


                #hacemos la consulta para eliminar el deatalle de venta
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

    def editar_detalle(self, id_detalle, id_articulo_nuevo, id_venta_nueva, nueva_cantidad):
        db = Generico()
        cur = None

        if db.conexion.is_connected():
            try:
                cur = db.conexion.cursor()
                
                # Paso 1: Buscar el detalle viejo para saber que articulo y cantidad habia antes
                cur.execute("SELECT id_articulo, cantidad FROM detalle_ventas WHERE id_detalle = %s", (id_detalle,))
                resultado_viejo = cur.fetchone()

                if not resultado_viejo:
                    print("Error: El ID de detalle no existe")
                    return False
                
                id_articulo_viejo = resultado_viejo[0]
                cantidad_vieja = resultado_viejo[1]

                # Paso 2: Buscar el precio y el stock actual del nuevo articulo elegido
                cur.execute("SELECT precio, stock FROM articulos WHERE id_articulo = %s", (id_articulo_nuevo,))
                resultado_articulo = cur.fetchone()

                if not resultado_articulo:
                    print("Error: El nuevo ID articulo no existe")
                    return False
                
                precio_articulo = resultado_articulo[0]
                stock_actual_nuevo = resultado_articulo[1]
                nuevo_sub_total = nueva_cantidad * precio_articulo

                # Paso 3: Calcular el stock real disponible sumando lo viejo si es el mismo articulo
                if id_articulo_nuevo == id_articulo_viejo:
                    stock_efectivo = stock_actual_nuevo + cantidad_vieja
                else:
                    stock_efectivo = stock_actual_nuevo

                # Paso 4: Si la nueva cantidad supera ese stock real, frena el proceso
                if nueva_cantidad > stock_efectivo:
                    print(f"Error: Stock insuficiente. El stock disponible real para la operacion es {stock_efectivo}.")
                    return False

                # Paso 5: Devolver la cantidad vieja al stock del articulo viejo
                cur.execute("UPDATE articulos SET stock = stock + %s WHERE id_articulo = %s", (cantidad_vieja, id_articulo_viejo))

                # Paso 6: Actualizar el detalle de la venta con los nuevos datos y el subtotal
                cur.execute("""
                    UPDATE detalle_ventas 
                    SET cantidad = %s, sub_total = %s, id_articulo = %s, id_venta = %s 
                    WHERE id_detalle = %s
                """, (nueva_cantidad, nuevo_sub_total, id_articulo_nuevo, id_venta_nueva, id_detalle))

                # Paso 7: Restar la nueva cantidad del stock del nuevo articulo
                cur.execute("UPDATE articulos SET stock = stock - %s WHERE id_articulo = %s", (nueva_cantidad, id_articulo_nuevo))

                # Paso 8: Guardar todos los cambios juntos con commit
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