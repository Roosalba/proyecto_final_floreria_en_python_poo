from generico import Generico
from proveedores import Proveedores
from metodo_pago import Metodo_pago
from categoria import Categoria
from articulos import Articulos
from clientes import Cliente
from ventas import Ventas
from detalle_venta import Detalle_venta

class Principal:
    def __init__(self):
        self.generico =Generico()
        self.proveedores = Proveedores()
        self.categoria = Categoria()
        self.metodo_pago= Metodo_pago()
        self.articulos = Articulos()
        self.clientes = Cliente()
        self.ventas = Ventas()
        self.detalle_venta = Detalle_venta()


    def menu_tabla(self):
        print("--EJECUTAR TABLAS--")
        print("1. Proveedores     ")
        print("2. Categoria       ")
        print("3. Articulos       ")
        print("4. Metodo_pago     ")
        print("5. Clientes        ")
        print("6. ventas          ")
        print("7. Detalle_venta   ")
        print("8. salir           ")

    def ejecutar_tablas(self):
        while True:
            self.menu_tabla()
            opcion_tabla=str(input("Ingrese el numero de la tabla a elijir:\n")).strip()

            if opcion_tabla =="":
                print("El campo no puede estar vacio")
                continue

            elif opcion_tabla =="1":
                print("Ingresate a la tabla Proveedores ")
                self.ejecutar_proveedor()
                
            elif opcion_tabla =="2":
                print("Ingresate a la tabla Categoria ")
                self.ejecutar_categoria()


            elif opcion_tabla =="3":
               print("Ingresate a la tabla Articulos ")
               self.ejecutar_articulos()


            elif opcion_tabla =="4":
                print("Ingresate a la tabla Metodo_pago ")
                self.ejecutar_metodo_pago()


            elif opcion_tabla =="5":
                print("Ingresate a la tabla Clientes ")
                self.ejecutar_clientes()


            elif opcion_tabla =="6":
                 print("Ingresate a la tabla Ventas ")
                 self.ejecutar_ventas()

            elif opcion_tabla =="7":
                 print("Ingresate a la tabla Detalle_ventas ")
                 self.ejecutar_detalle_ventas()

            elif opcion_tabla =="8":
                print("Saliendo del menu de tablas")
                break
            
            else:
                print("Opcion incorrecta")

    def menuCrud(self):
        print("LISTADO DE OPCIONES")
        print("1.Ingresar ")
        print("2.Listar ")
        print("3.Buscar ")
        print("4.Editar ")
        print("5.Borrar ")
        print("6.Salir")

    def ejecutar_proveedor(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar proveedores")
                while True:
                    nombre_empresa=str(input("Ingrese el nombre de la empresa: ")).strip()
                    
                    if nombre_empresa=="":
                        print("El campo no puede estar vacio")
                        continue
                    break
                    
                while True:
                    telefono=str(input("Ingrese el numero de telefono: ")).strip()
                    if telefono =="":
                        print("El campo no puede estar vacio")
                        continue
                
                    
                    if self.proveedores.buscar_por_telefono(telefono) is not None:
                        print("El telefono ya existe en el sistema. Ingrese otro.")
                        continue
                    break
                            
                datos=self.proveedores.registrar_proveedores(nombre_empresa,telefono)
                if datos:
                    print("Datos registrado  correctamente")
                else:
                    print("Hubo un error al registrar los datos del proveedor")
                    
            elif opcionMenu =="2":
                print("Listar proveedores")
                lista=self.proveedores.listar_proveedores()
                if not lista:
                    print("No hay proveedores para mostrar")
                else:
                    for prove in lista:
                        print(f"ID:{prove[0]} | NOMBRE:{prove[1]} | TELEFONO:{prove[2]}")

            elif opcionMenu =="3":
                print("Buscar proveedor")
                while True:
                        buscar_telefono=str(input("Ingrese el telefono a buscar, '0' para salir: ")).strip()
                        if buscar_telefono=="":
                            print("El campo no puede estar vacio")
                            continue
                        if buscar_telefono=="0":# esta la coloque por s el usuario quiere salir sin hacer nada
                            print("volviendo al menu principal de proveedores.")
                            break
                        buscando_tele=self.proveedores.buscar_por_telefono(buscar_telefono)
                        if  buscando_tele is None:
                            print("No se encontro el proveedor con ese telefono.")
                            continue
                        else:
                            print(f"ID: {buscando_tele[0]} | NOMBRE: {buscando_tele[1]} | TELEFONO: {buscando_tele[2]}")
                            break
                    
            elif opcionMenu =="4":
                print("Editar Proveedor")
                while True:
                    try:
                        id_editar=int(input("Ingrese el ID a editar, 0 para volver al menu de proveedores: "))
                        if id_editar==0:
                            print("Volviendo al menu de proveedores..")
                            break
                        editando_id=self.proveedores.buscar_por_id(id_editar)
                        if editando_id:

                            break
                        else:
                            print(f"El ID: {id_editar} no se encontro")
                    except ValueError:
                        print("El ID debe ser un numero entero")
                            
                if id_editar==0:
                    continue
                   
                while True:
                    nuevo_nombre=str(input("Nuevo Nombre: ")).strip()
                    if nuevo_nombre=="":
                        print("Ela campo no puede estar vacio")
                        continue
                    break
                while True:
                    nuevo_telefono=str(input("Nuevo telefono: ")).strip()
                    if nuevo_telefono=="":
                        print("El campo no puede estar vacio")
                        continue
                    break
                        # Guardamos los cambios llamando al  metodo de editar
                if self.proveedores.editar_proveedor(nuevo_nombre,nuevo_telefono,id_editar):
                    print("Proveedores editado con exito")
                else:
                    print("Error al guardar los cambios")

                            

            elif opcionMenu =="5":
                print("eliminar proveedor")

                while True:
                        try:
                            id_eliminar=int(input("Ingrese el ID a eliminar, 0 para salir: "))
                            if id_eliminar==0:# esta la coloque por s el usuario quiere salir sin hacer nada
                                print("volviendo al menu principal de Proveedores.")
                                break
                        except ValueError:
                            print("Error debe ingresar un numero") 
                            continue
                        eliminado_exitoso=self.proveedores.eliminar_proveedor(id_eliminar)
                        if not eliminado_exitoso:
                            print(f"No existe ningun proveedor con el Id {id_eliminar}. Intente de nuevo")
                            continue
                        else:
                            print("Proveedor eliminado con exito")
                            break


            elif opcionMenu =="6":
                print("Saliendo del menuCrud de proveedores")
                break
            else:

                print("Opcion incorrecta")

    def ejecutar_categoria(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar Categoria")
                while True:
                    nombre_categoria=str(input("Ingrese el nombre de la categoria: ")).strip()
                    if nombre_categoria=="":
                        print("El campo no puede estar vacio ")
                        continue
                    break
                exito=self.categoria.registrar_categoria(nombre_categoria)

                if exito:
                    print("La categoria fue registrada con existo")
                    
                else:
                    print("Hubo un error al registrar el nombre de la categoria")

            elif opcionMenu =="2":
                print("Listar Categoria")
                lista=self.categoria.listar_categoria()

                if not lista:
                    print("No hay categoria para mostrar")
                else:
                    #Recorremos la lista categoria
                    for cate in lista:
                       print(f"ID:{cate[0]} | NOMBRE:{cate[1]} ")

            elif opcionMenu =="3":
                print("Buscar Categoria")
                while True:
                    try:
                        buscar_id=int(input("Ingrese el id a buscar, '0' para salir: "))
                        if buscar_id==0:
                            print("volviendo al menu principal.")
                            break
                        buscando_id=self.categoria.buscar_categoria(buscar_id)
                        if not buscando_id:
                            print("No se encontro la categoria con ese ID.")
                        else:
                            print(f"ID: {buscando_id[0]} | NOMBRE: {buscando_id[1]}")
                            
                    except ValueError:
                        print("Debe ingresar un numero ")

            
            elif opcionMenu =="4":
                print("Editar Categoria")
                while True:
                    try:
                        editar_id=int(input("Ingrese el ID a editar, 0 para salir :"))
                        if editar_id==0:
                            print("volviendo al menu principal de categoria.")
                            break
                        editando_id=self.categoria.buscar_categoria(editar_id)
                        if  editando_id:
                            break #Si encuentra el ID, Rompemos este bucle y avanza para pedir los datos, sino se esjecuta el else
                        else:
                            print(f"El ID {editar_id} no existe en la base de datos intente de nuevo")
                    except ValueError:
                        print("El ID debe ser un numero entero")
                        continue
                # este es para cuando el usuario escriba 0, vuelva arriba y no me pida editar datos            
                if editar_id==0:
                    continue

                while True:
                    nuevo_nombre=str(input("Nuevo Nombre: ")).strip()
                    if nuevo_nombre=="":
                        print("Ela campo no puede estar vacio")
                        continue
                    break
                 # Guardamos los cambios llamando al  metodo de editar
                if self.categoria.editar_categoria(editar_id,nuevo_nombre):
                    print("Catalogo editado con exito")
                else:
                    print("Error al guardar los cambios")


            elif opcionMenu =="5":
                print("eliminar Categoria")
                while True:
                    try:
                        id_eliminar=int(input("Ingrese el ID a eliminar '0' para salir del menu:"))
                        if id_eliminar==0:
                            break
                        eliminando=self.categoria.eliminar_categoria(id_eliminar)
                        if eliminando:
                            print("Catagolo eliminado con exito")
                            break
                        else:
                            print(f"No existe ningun catalogo con ese ID {id_eliminar}.Intente de nuevo")

                    except ValueError:
                        print("Error debe ingresar un numero")
                        continue

            elif opcionMenu =="6":
                print("Saliendo del menuCrud de Categoria")
                break
            else:

                print("Opcion incorrecta")



    def ejecutar_articulos(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar Articulos ")
                # 1. VALIDAMOS EL ID DE PROVEEDORES
                while True:
                    try:
                        id_proveedor=int(input("Ingrese el ID del proveedor: "))
                        if id_proveedor==0:
                            print("Operacion cancelada.")
                            break

                        buscar_id_proveedor=self.proveedores.buscar_por_id(id_proveedor)
                        if buscar_id_proveedor is None:
                            print(f"Error: El proveedor con ID {id_proveedor} no existe.Intente nuevamente ")
                            continue
                        break
                    except ValueError:
                        print("Error: El ID debe ser un numero entero.")
                
                    if id_proveedor==0:
                        continue # regresa al  menu de opciones
                     # 2. VALIDAMOS EL ID DE CATEGORIA

                while True:               
                    try:
                        id_categoria=int(input("Ingrese el ID de categoria: "))
                        if id_categoria==0:
                            print("Operacion cancelada.")
                            break

                        buscar_id_categoria=self.categoria.buscar_categoria(id_categoria)
                        if buscar_id_categoria is None:# validamos si existe el id de categoria
                            print(f"Error: La categoria con ID {id_categoria} no existe ")
                            continue
                        break
                    except ValueError:
                        print("Error: El ID debe ser un numero entero.")

                    if id_categoria==0:
                        continue

                # 3. PEDIR EL NOMBRE DEL ARTÍCULO
                while True:
                    nombre=str(input("Ingrese el nombre del articulo: ")).strip()
                    if nombre=="":
                        print("El campo no puede estar vacio")
                        continue
                    break

                    # 4. PEDIR EL PRECIO DEL ARTÍCULO
                while True:
                        try:
                            precio=float(input("Ingrese el precio del articulo: "))
                            if precio <= 0:
                                print("El precio debe ser un numero positivo")
                                continue
                            break
                        except ValueError:
                            print("Error: el precio debe ser un numero decimal")

                   # 4. PEDIR EL STOC DEL ARTÍCULO         
                while True:
                        try:
                            stock=int(input("Ingrese el stock del artiulo: "))
                            if stock <= 0:
                                print("El stock debe ser mayor a cero")
                                continue
                            break
                        except ValueError:
                            print("Error: el precio debe ser un numero entero")

                # 5. GUARDAR EN LA BASE DE DATOS
                resultado=self.articulos.agregar_articulos(nombre,precio,stock,id_proveedor,id_categoria)
                if resultado: 
                        print("Articulo guardado con exito")
                else:
                    print("Error: No se pudo guardar el articulo en la base de datos")
                   
               


            elif opcionMenu =="2":
                print("Listar Articulos ")
                lista=self.articulos.listar_articulos()

                if not lista:
                    print("No hay ARTICULOS para mostrar")
                else:
                    #Recorremos la lista ARTICULOS
                    for articulo in lista:
                       print(f"ID:{articulo[0]} | NOMBRE:{articulo[1]}  | PRECIO:{articulo[2]} | STOCK:{articulo[3]} | ID_PROVEEDOR:{articulo[4]} | ID_CATEGORIA:{articulo[5]}")


            elif opcionMenu =="3":
                print("Buscar Articulos ")
                while True:
                    try:
                        buscar_id=int(input("Ingrese el id a buscar, '0' para salir: "))
                        if buscar_id==0:
                            print("volviendo al menu principal.")
                            break
                        buscando_id=self.articulos.buscar_articulos(buscar_id)
                        if not buscando_id:
                            print("No se encontro el articulo con ese ID.")
                        else:
                            print(f"ID: {buscando_id[0]} | NOMBRE: {buscando_id[1]} | PRECIO: {buscando_id[2]} | STOCK: {buscando_id[3]} | ID_PROVEEDOR: {buscando_id[4]} | ID_CATEGORIA: {buscando_id[5]}")
                            
                    except ValueError:
                        print("Debe ingresar un numero ")

            
            elif opcionMenu =="4":
                print("Editar Articulos")
            # 1. VALIDAR ID DEL ARTÍCULO
                while True:
                    try:
                        id_editar = int(input("Ingrese el ID a editar o 0 para salir: "))
                        if id_editar == 0:
                            print("Operación cancelada.")
                            break
                        
                        buscando_id = self.articulos.buscar_articulos(id_editar)
                        if buscando_id is None:
                            print(f"Error: El ID {id_editar} no existe en la base de datos. Intente nuevamente.")
                            continue
                        
                        break # ID válido y existe, salimos de este bucle
                    except ValueError:
                        print("Error: El ID debe ser un número entero.")
                        continue

                if id_editar == 0:
                    continue # Vuelve al menú principal si el usuario canceló

                # 2. VALIDAR ID DEL PROVEEDOR
                while True:
                    try:
                        id_proveedor = int(input("Ingrese el ID del proveedor o presione '0' para volver al menú principal: "))
                        if id_proveedor == 0:
                            print("Operación cancelada.")
                            break
                            
                        buscar_id_proveedor = self.proveedores.buscar_por_id(id_proveedor)
                        if buscar_id_proveedor is None:
                            print(f"Error: El proveedor con ID {id_proveedor} no existe.")
                            continue
                            
                        break # Proveedor válido, salimos del bucle
                    except ValueError:
                        print("Error: El ID del proveedor debe ser un número entero.")

                if id_proveedor == 0:
                    continue

                # 3. VALIDAR ID DE CATEGORÍA
                while True:
                    try:
                        id_categoria = int(input("Ingrese el ID de categoría o presione '0' para volver al menú principal: "))
                        if id_categoria == 0:
                            print("Operación cancelada.")
                            break
                            
                        buscar_id_categoria = self.categoria.buscar_categoria(id_categoria)
                        if buscar_id_categoria is None:
                            print(f"Error: La categoría con ID {id_categoria} no existe.")
                            continue
                            
                        break # Categoría válida, salimos del bucle
                    except ValueError:
                        print("Error: El ID de la categoría debe ser un número entero.")

                if id_categoria == 0:
                    continue         

                # 4. PEDIR NUEVO NOMBRE
                while True:
                    nuevo_nombre = str(input("Ingrese el nombre del artículo: ")).strip()
                    if nuevo_nombre == "":
                        print("El campo no puede estar vacío.")
                        continue
                    break

                # 5. PEDIR NUEVO PRECIO
                while True:
                    try:
                        nuevo_precio = float(input("Ingrese el precio del artículo: "))
                        if nuevo_precio <= 0:
                            print("El precio debe ser un número positivo.")
                            continue
                        break
                    except ValueError:
                        print("Error: el precio debe ser un número decimal.")

                # 6. PEDIR NUEVO STOCK
                while True:
                    try:
                        nuevo_stock = int(input("Ingrese el stock del artículo: "))
                        if nuevo_stock < 0:
                            print("El stock debe ser mayor o igual a cero.")
                            continue
                        break
                    except ValueError:
                        print("Error: el stock debe ser un número entero.")

                # 7. GUARDAR CAMBIOS EN LA BASE DE DATOS
                resultado = self.articulos.editar_articulos(id_editar, nuevo_nombre, nuevo_precio, nuevo_stock, id_proveedor, id_categoria)
                
                if resultado:
                    print("¡Artículo editado con éxito!")
                else:
                    print("No se pudo editar el artículo (Verificá si hubo cambios o errores en la base de datos).")
                                

            elif opcionMenu =="5":
                print("eliminar Articulos ")
                while True:
                    try:
                        id_eliminar=int(input("Ingrese el ID a eliminar '0' para salir del menu:"))
                        if id_eliminar==0:
                            break
                        eliminando=self.articulos.eliminar_articulos(id_eliminar)
                        if eliminando:
                            print("Articulo eliminado con exito")
                            break
                        else:
                            print(f"No existe ningun ARTICULO con ese ID {id_eliminar}.Intente de nuevo")

                    except ValueError:
                        print("Error debe ingresar un numero")
                        continue


            elif opcionMenu =="6":
                print("Saliendo del menuCrud de Articulos ")
                break
            else:

                print("Opcion incorrecta")

    def ejecutar_metodo_pago(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar Metedo de Pago")

                while True:
                    nombre_metodo=str(input("Ingrese el metodo de pago: ")).strip()
                    if nombre_metodo=="":
                        print("El campo no puede estar vacio ")
                        continue
                    break
                exito=self.metodo_pago.registrar_metedo_pago(nombre_metodo)

                if exito:
                    print("el metodo de pago fue registrado con existo")
                    
                else:
                    print("Hubo un error al registrar el metodo de pago")


            elif opcionMenu =="2":
                print("Listar Metodo de Pago ")
                lista=self.metodo_pago.listar_metodo_pago()

                if not lista:
                    print("No hay metodo de pago para mostrar")
                else:
                    #Recorremos la lista de metodos pago
                    for pago in lista:
                       print(f"ID:{pago[0]} | METODO_PAGO:{pago[1]} ")



            elif opcionMenu =="3":
                print("Buscar Metodo de pago")
                while True:
                    try:
                        buscar_id=int(input("Ingrese el id a buscar, '0' para salir: "))
                        if buscar_id==0:
                            print("volviendo al menu principal.")
                            break
                        buscando_id=self.metodo_pago.buscar_metodo_pago(buscar_id)
                        if not buscando_id:
                            print("No se encontro el metodo de pago con ese ID.")
                        else:
                            print(f"ID:{buscando_id[0]} | METODO_PAGO:{buscando_id[1]}")
                            
                    except ValueError:
                        print("Debe ingresar un numero ")

            
            elif opcionMenu =="4":
                print("Editar Metodo de pago ")

                while True:
                    try:
                        editar_id=int(input("Ingrese el ID a editar, 0 para salir :"))
                        if editar_id==0:
                            print("volviendo al menu principal de metodo pago.")
                            break
                        editando_id=self.metodo_pago.buscar_metodo_pago(editar_id)
                        if editando_id:
                            break #Si encuentra el ID, Rompemos este bucle y avanza para pedir los datos, sino se esjecuta el else
                        else:
                            print(f"El ID {editar_id} no existe en la base de datos intente de nuevo")
                            continue
                    except ValueError:
                        print("El ID debe ser un numero entero")
                        continue
                # este es para cuando el usuario escriba 0, vuelva arriba y no me pida editar datos            
                if editar_id==0:
                    continue

                while True:
                    nuevo_metodo_pago=str(input("Nuevo Metodo_pago: ")).strip()
                    if nuevo_metodo_pago=="":
                        print("Ela campo no puede estar vacio")
                        continue
                    break
                    # Guardamos los cambios llamando al  metodo de editar
                if self.metodo_pago.editar_metodo_pago(editar_id,nuevo_metodo_pago):
                    print("Metodo de pago editado con exito")
                else:
                    print("Error al guardar los cambios")
                

            elif opcionMenu =="5":
                print("eliminar Metodo de pago")
                while True:
                    try:
                        id_eliminar=int(input("Ingrese el ID a eliminar '0' para salir del menu:"))
                        if id_eliminar==0:
                            break
                        eliminando=self.metodo_pago.eliminar_metodo_pago(id_eliminar)
                        if eliminando:
                            print("metodo de pago eliminado con exito")
                            break
                        else:
                            print(f"No existe ningun metodo de pago con ese ID {id_eliminar}.Intente de nuevo")

                    except ValueError:
                        print("Error debe ingresar un numero")
                        continue




            elif opcionMenu =="6":
                print("Saliendo del menuCrud de Metodo de pago ")
                break
            else:

                print("Opcion incorrecta")




    def ejecutar_clientes(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar Clientes")
                while True:
                    try:
                        id_cliente=int(input("Ingrese el ID del cliente: "))
                        verificar=self.clientes.buscar_clientes(id_cliente)
                        if verificar:
                            print("El cliente ya existe. Intente nuevamente")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Error: El ID debe ser un numero entero.")
                        continue
                # ingresamos los datos despues de validar el ID
                while True:
                    nombre=str(input("Ingrese el nombre del cliente: ")).strip()
                    if nombre=="":
                        print("El campo no puede estar vacio")
                        continue
                    break
                while True:
                    telefono=str(input("Ingrese el numero de telefono: ")).strip()
                    if telefono=="":
                        print("El campo no puede estar vacio.")
                        continue
                    break
                while True:
                    email=str(input("Ingrese el correo: ")).strip()
                    if email=="":
                        print("El campo no puede estar vacio.")
                        continue
                    break
                if self.clientes.agregar_clientes(id_cliente,nombre,telefono,email):
                    print("Cliente registrado con exito.")
                else:
                    print("Error al agregar al cliente en la base de datos")
                    

            elif opcionMenu =="2":
                print("Listar Clientes")
                lista=self.clientes.listar_cliente() # guardamos en la variable lista lo que retornamos
                # validamos
                if not lista:
                    print("No hay Clientes")
                    continue
                else:
                    for clientes in lista:
                     print(f"ID: {clientes[0]}, NOMBRE: {clientes[1]}, TELEFONO: {clientes[2]}, EMAIL: {clientes[3]} ")



            elif opcionMenu =="3":
                print("Buscar Clientes ")
                while True:
                    try:
                        buscar_id=int(input("Ingrese el id a buscar, '0' para salir: "))
                        if buscar_id==0:
                            print("volviendo al menu principal.")
                            break
                        buscando_id=self.clientes.buscar_clientes(buscar_id)
                        if not buscando_id:
                            print("No se encontro el cliente con ese ID.")
                        else:
                            print(f"ID:{buscando_id[0]} | NOMBRE:{buscando_id[1]} | TELEFONO:{buscando_id[2]} | EMAIL:{buscando_id[3]}")
                            
                    except ValueError:
                        print("Debe ingresar un numero ")


            
            elif opcionMenu =="4":
                print("Editar Clientes")

                while True:
                    try:
                        id_editar=int(input("Ingrese el ID a editar, 0 para volver al menu de proveedores: "))
                        if id_editar==0:
                            print("Volviendo al menu de clientes..")
                            break
                        editando_id=self.clientes.buscar_clientes(id_editar)
                        if editando_id:

                            break
                        else:
                            print(f"El ID: {id_editar} no se encontro")
                    except ValueError:
                        print("El ID debe ser un numero entero")
                            
                if id_editar==0:
                    continue
                   
                while True:
                    nuevo_nombre=str(input("Nuevo Nombre: ")).strip()
                    if nuevo_nombre=="":
                        print("Ela campo no puede estar vacio")
                        continue
                    break
                while True:
                    nuevo_telefono=str(input("Nuevo telefono: ")).strip()
                    if nuevo_telefono=="":
                        print("El campo no puede estar vacio")
                        continue
                    break
                        # Guardamos los cambios llamando al  metodo de editar

                while True:
                    nuevo_email=str(input("Nuevo Email: ")).strip()
                    if nuevo_email=="":
                        print("El campo no puede estar vacio.")
                        continue
                    break
                #lo hice directo sin crear la variable
                if self.clientes.editar_clientes(id_editar,nuevo_nombre,nuevo_telefono,nuevo_email):
                    print("Clientes editado con exito")
                else:
                    print("Error al guardar los cambios")

            elif opcionMenu =="5":
                print("eliminar Clientes ")
                while True:
                    try:
                        id_eliminar=int(input("Ingrese el ID a eliminar '0' para salir del menu:"))
                        if id_eliminar==0:
                            break
                        eliminando=self.clientes.eliminar_cliente(id_eliminar)
                        if eliminando:
                            print("El cliente fue eliminado con exito")
                            break
                        else:
                            print(f"No existe ningun cliente con ese ID {id_eliminar}.Intente de nuevo")

                    except ValueError:
                        print("Error debe ingresar un numero")
                        continue


            elif opcionMenu =="6":
                print("Saliendo del menuCrud de Clientes ")
                break
            else:

                print("Opcion incorrecta")



    def ejecutar_ventas(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar Ventas")
                # 1. VALIDAR ID DEL CLIENTE
                while True:
                    try:
                        id_cliente=int(input("Ingrese el ID del cliente (o 0 para cancelar): "))
                        if id_cliente==0:
                            print("Operacion cancelada.")
                            break
                        # buscamos y validamos el id del cliente, sino existe nos pide nuevamante
                        buscar_id_cliente=self.clientes.buscar_clientes(id_cliente)
                        if not buscar_id_cliente:
                            print(f"Error: El cliente con ID {id_cliente} no existe. Intente nuevamente.")
                            continue
                        else:
                            break # si el ID existe, sale de este bucle
                    except ValueError:
                        print("Error: El ID debe ser un numero entero.")
                        continue

                if id_cliente==0:
                    continue # este lo coloco aca, para tener la opcion de volver al menu principal de ventas


                # 2. VALIDAR ID DEL MÉTODO DE PAGO
                while True:
                   try:
                       id_metodo_pago=int(input("Ingrese el ID del metodo de pago (o 0 para salir):"))
                       if id_metodo_pago==0:
                           print("Operacion cancelada")
                           break
                       #si no existe en la bases de datos, da error y pide nuevamnete
                       buscar_id_metodo=self.metodo_pago.buscar_metodo_pago(id_metodo_pago)
                       if not buscar_id_metodo:
                            print(f"Error: El método de pago con ID {id_metodo_pago} no existe. Intente nuevamente.")
                            continue
                       break
                   except ValueError:
                         print("Error: El ID debe ser un número entero.")

                if id_metodo_pago == 0:
                    continue # Nos saca al menú principal si canceló 

                # 3. EL TOTAL DE LA VENTA LO DEJO EN 0
                total_venta=0.0
                print(f"Generando factura con total inicial: ${total_venta}")
                # 4. GUARDAR EN LA BASE DE DATOS
                id_venta_generada = self.ventas.agregar_ventas(total_venta, id_cliente, id_metodo_pago)
                
                if id_venta_generada:
                    print(f"¡Venta registrada con éxito! ID asignado: {id_venta_generada}")
                    print("RECUERDE: Ahora vaya al menu de 'Detalle_venta' para cargar los articulos de esta venta.")
                else:
                    print("Error: No se pudo registrar la venta.")


                            

            elif opcionMenu =="2":
                print("Listar Ventas ")
                lista=self.ventas.listar_ventas() # guardamos en la variable lista lo que retornamos
                # validamos
                if not lista:
                    print("No hay ventas")
                    continue
                else:
                    for venta in lista:
                     print(f"ID: {venta[0]}, FECHA: {venta[1]}, TOTAL: {venta[2]}, ID_CLIENTE: {venta[3]},  ID_METODO_PAGO: {venta[4]} ")




            elif opcionMenu =="3":
                print("Buscar Ventas ")
                while True:
                    try:
                        buscar_id=int(input("Ingrese el id a buscar, '0' para salir: "))
                        if buscar_id==0:
                            print("volviendo al menu principal ve ventas.")
                            break
                    
                        buscando_id=self.ventas.buscar_venta(buscar_id)
                        if not buscando_id:
                            print("No se encontra la venta con ese ID.")
                            continue
                        else:
                            print(f"ID:{buscando_id[0]} | FECHA:{buscando_id[1]} | TOTAL:{buscando_id[2]} | ID_CLIENTE:{buscando_id[3]} | ID_METODO_PAGO:{buscando_id[4]} ")
                            break      
                    except ValueError:
                        print("Debe ingresar un numero ")
                        continue

            
            elif opcionMenu =="4":
                print("Editar Ventas")
                # 1. VALIDAMOS EL ID DE VENTAS
                while True:
                    try:
                        id_editar = int(input("Ingrese el ID a editar o 0 para salir: "))
                        if id_editar == 0:
                            print("Operación cancelada.")
                            break
                        
                        buscando_id = self.ventas.buscar_venta(id_editar)
                        if buscando_id is None:
                            print(f"Error: El ID {id_editar} no existe en la base de datos. Intente nuevamente.")
                            continue
                        
                        break # ID válido y existe, salimos de este bucle
                    except ValueError:
                        print("Error: El ID debe ser un número entero.")
                        continue

                if id_editar == 0:
                    continue # Vuelve al menú principal si el usuario canceló

                # 2. VALIDAR ID DEL CLIENTE
                while True:
                    try:
                        id_cliente = int(input("Ingrese el ID del cliente o presione '0' para volver al menú principal: "))
                        if id_cliente == 0:
                            print("Operación cancelada.")
                            break
                            
                        buscar_id_cliente = self.clientes.buscar_clientes(id_cliente)
                        if buscar_id_cliente is None:
                            print(f"Error: El cliente con ID {id_cliente} no existe.")
                            continue
                            
                        break # Proveedor válido, salimos del bucle
                    except ValueError:
                        print("Error: El ID del cliente debe ser un número entero.")

                if id_cliente == 0:
                    continue

                # 3. VALIDAR ID DEL METODO DE PAGO
                while True:
                    try:
                        id_metodo_pago = int(input("Ingrese el ID del metodo de pago o presione '0' para volver al menú principal: "))
                        if id_metodo_pago == 0:
                            print("Operación cancelada.")
                            break
                            
                        buscar_id_metodo_pago = self.metodo_pago.buscar_metodo_pago(id_metodo_pago)
                        if buscar_id_metodo_pago is None:
                            print(f"Error: El metodo de pago con ID {id_metodo_pago} no existe.")
                            continue
                            
                        break # metodo de pago válida, salimos del bucle
                    except ValueError:
                        print("Error: El ID de la categoría debe ser un número entero.")

                if id_metodo_pago == 0:
                    continue         

               
                # 5. GUARDAR CAMBIOS EN LA BASE DE DATOS
                resultado = self.ventas.editar_venta(id_editar,id_cliente,id_metodo_pago)
                if resultado:
                    print("¡venta editada con éxito!")
                else:
                    print("No se pudo editar la venta (Verificá si hubo cambios o errores en la base de datos).")
                                

            elif opcionMenu =="5":
                print("eliminar Ventas ")
                while True:
                    try:
                        id_eliminar=int(input("Ingrese el ID a eliminar '0' para salir del menu:"))
                        if id_eliminar==0:
                            break
                        eliminando=self.ventas.eliminar_venta(id_eliminar)
                        if eliminando:
                            print("la venta fue eliminado con exito")
                            break
                        else:
                            print(f"No existe ninguna venta con ese ID {id_eliminar}.Intente de nuevo")

                    except ValueError:
                        print("Error debe ingresar un numero")
                        continue



            elif opcionMenu =="6":
                print("Saliendo del menuCrud de Ventas ")
                break
            else:

                print("Opcion incorrecta")


    def ejecutar_detalle_ventas(self):
        while True:
            self.menuCrud()
            opcionMenu=str(input("Ingrese la opcion del 1 al 6: ")).strip()

            if opcionMenu =="":
                print("El campo no puede estar vacio")
                continue

            elif opcionMenu =="1":
                print("Ingresar detalle ventas ")

                # 1.VALIDAR EL ID DEL ARTICULO
                while True:
                    try:
                        id_articulo=int(input("Ingrese el ID del articulo (o 0 para cancelar): "))
                        if id_articulo==0:
                            print("Operacion cancelada.")
                            break
                        # buscamos y validamos el id del articulo, sino existe nos pide nuevamante
                        buscar_id_articulo=self.articulos.buscar_articulos(id_articulo)
                        if not buscar_id_articulo:
                            print(f"Error: El articulo con ID {id_articulo} no existe. Intente nuevamente.")
                            continue
                        else:
                            #Me trae el precio del ariculo mediante su indice, para hacer el subtotal
                            precio_articulo=buscar_id_articulo[2]
                            stock_disponible=buscar_id_articulo[3]
                            break # si el ID existe, sale de este bucle
                    except ValueError:
                        print("Error: El ID debe ser un numero entero.")
                        continue

                if id_articulo==0:
                    continue # este lo coloco aca, para tener la opcion de volver al menu principal de ventas


                # 2. VALIDAR ID DE LA VENTA
                while True:
                   try:
                       id_venta=int(input("Ingrese el ID  de la venta (o 0 para salir):"))
                       if id_venta==0:
                           print("Operacion cancelada")
                           break
                       #si no existe en la bases de datos, da error y pide nuevamnete
                       buscar_id_metodo=self.ventas.buscar_venta(id_venta)
                       if not buscar_id_metodo:
                            print(f"Error: La venta con ID {id_venta} no existe. Intente nuevamente.")
                            continue
                       break
                   except ValueError:
                         print("Error: El ID debe ser un número entero.")

                if id_venta == 0:
                    continue # Nos saca al menú principal si canceló 

                # 3. PEDIR LA CANTIDAD 
                while True:
                    try:
                        cantidad =int(input("Ingrese la cantidad : "))
                        if cantidad <= 0:
                            print("El precio debe ser un número positivo.")
                            continue
                        if cantidad > stock_disponible:
                            print(f"Error: NO hay suficiente stock. Solo quedan {stock_disponible} unidades. Intente nuevamente")
                            continue
                        break
                    except ValueError:
                        print("Error: La cantidad debe ser un numero entero.")


                # 4. CALCULAR EL SUBTOTAL AUTOMÁTICAMENTE 
                sub_total=cantidad*precio_articulo


                # 5. GUARDAR EN LA BASE DE DATOS
                resultado = self.detalle_venta.agregar_detalle_venta(cantidad,sub_total,id_articulo,id_venta)
                
                if resultado:
                    print(f"¡Detalle de Venta registrada con éxito! ")
                else:
                    print("Error: No se pudo registrar la venta.")



            elif opcionMenu =="2":
                print("Listar detalle ventas ")
                lista=self.detalle_venta.listar_detalle_ventas() # guardamos en la variable lista lo que retornamos
                # validamos
                if not lista:
                    print("No hay detalles de ventas para mostrar")
                    continue
                else:
                    for venta in lista:
                     print(f"ID: {venta[0]}, CANTIDAD: {venta[1]}, SUB_TOTAL: {venta[2]}, ID_ARTICULO: {venta[3]},  ID_VENTA: {venta[4]} ")



            elif opcionMenu =="3":
                print("Buscar detalle ventas")
                while True:
                    try:
                        buscar_id=int(input("Ingrese el id a buscar, '0' para salir: "))
                        if buscar_id==0:
                            print("volviendo al menu principal ve ventas.")
                            break
                    
                        buscando_id=self.detalle_venta.buscar_detalle_ventas(buscar_id)
                        if not buscando_id:
                            print("No se encontro el detalle de venta con ese ID.")
                            continue
                        else:
                            print(f"ID:{buscando_id[0]} | CANTIDAD:{buscando_id[1]} | SUB_TOTAL:{buscando_id[2]} | ID_ARTICULO:{buscando_id[3]} | ID_VENTA:{buscando_id[4]} ")
                            break      
                    except ValueError:
                        print("Debe ingresar un numero ")
                        continue
                

            
            elif opcionMenu =="4":
                print("Editar detalles ventas ")
                # 1. VALIDAMOS EL ID DE DETALLE
                while True:
                    try:
                        id_editar = int(input("Ingrese el ID a editar o 0 para salir: "))
                        if id_editar == 0:
                            print("Operación cancelada.")
                            break
                        
                        buscando_id = self.detalle_venta.buscar_detalle_ventas(id_editar)
                        if buscando_id is None:
                            print(f"Error: El ID {id_editar} no existe en la base de datos. Intente nuevamente.")
                            continue
                        
                        break # ID válido y existe, salimos de este bucle
                    except ValueError:
                        print("Error: El ID debe ser un número entero.")
                        continue

                if id_editar == 0:
                    continue # Vuelve al menú principal si el usuario canceló

                 # 2. VALIDAR ID DEL ARTICULO
                while True:
                    try:
                        id_articulo = int(input("Ingrese el ID del articulo o presione '0' para volver al menú principal: "))
                        if id_articulo == 0:
                            print("Operación cancelada.")
                            break
                            
                        buscar_id_articulo = self.articulos.buscar_articulos(id_articulo)
                        if buscar_id_articulo is None:
                            print(f"Error: El articulo con ID {id_articulo} no existe.")
                            continue
                            
                        break # metodo de pago válida, salimos del bucle
                    except ValueError:
                        print("Error: El ID del articulo debe ser un número entero.")

                if id_articulo == 0:
                    continue         


                # 3. VALIDAR ID DE LA VENTA
                while True:
                    try:
                        id_venta= int(input("Ingrese el ID de la venta o presione '0' para volver al menú principal: "))
                        if id_venta == 0:
                            print("Operación cancelada.")
                            break
                            
                        buscar_id_venta = self.ventas.buscar_venta(id_venta)
                        if buscar_id_venta is None:
                            print(f"Error: La venta con ID {id_venta} no existe.")
                            continue
                            
                        break # Proveedor válido, salimos del bucle
                    except ValueError:
                        print("Error: El ID de la venta debe ser un número entero.")

                if id_venta == 0:
                    continue


                # 4. SOLICITAR LA NUEVA CANTIDAD (
                while True:
                    try:
                        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                        if nueva_cantidad <= 0:
                            print("Error: La cantidad debe ser mayor a 0.")
                            continue
                        
                        break # Cantidad valida, salimos del bucle
                    except ValueError:
                        print("Error: La cantidad debe ser un número entero.")
                        
                # 5. GUARDAR CAMBIOS EN LA BASE DE DATOS
                resultado = self.detalle_venta.editar_detalle(id_editar,id_articulo,id_venta,nueva_cantidad)
                if resultado:
                    print("¡detalle de venta editada con éxito!")
                else:
                    print("No se pudo editar el detalle de venta (Verificá si hubo cambios o errores en la base de datos).")
                                

                
            elif opcionMenu =="5":
                print("eliminar detalle ventas ")
                while True:
                    try:
                        id_eliminar=int(input("Ingrese el ID a eliminar '0' para salir del menu:"))
                        if id_eliminar==0:
                            break
                        eliminando=self.detalle_venta.eliminar_detalle(id_eliminar)
                        if eliminando:
                            print("el detalle de venta fue eliminado con exito")
                            break
                        else:
                            print(f"No existe ningun detalle de venta con ese ID {id_eliminar}.Intente de nuevo")

                    except ValueError:
                        print("Error debe ingresar un numero")
                        continue


            elif opcionMenu =="6":
                print("Saliendo del menuCrud de detalles de ventas")
                break
            else:

                print("Opcion incorrecta")
if __name__ == "__main__":
    principal=Principal()
    principal.ejecutar_tablas()