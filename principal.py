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
        print("1. Proveedores   ")
        print("2. Categoria     ")
        print("3. Articulos     ")
        print("4. Metodo_pago   ")
        print("5. Clientes      ")
        print("6. ventas        ")
        print("7. Detalle_venta ")
        print("8. salir         ")

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

            elif opcionMenu =="2":
                print("Listar Articulos ")


            elif opcionMenu =="3":
                print("Buscar Articulos ")

            
            elif opcionMenu =="4":
                print("Editar Articulos")

            elif opcionMenu =="5":
                print("eliminar Articulos ")


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

            elif opcionMenu =="2":
                print("Listar Metodo de Pago ")


            elif opcionMenu =="3":
                print("Buscar Metodo de pago")

            
            elif opcionMenu =="4":
                print("Editar Metodo de pago ")

            elif opcionMenu =="5":
                print("eliminar Metodo de pago")


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

            elif opcionMenu =="2":
                print("Listar Clientes")
                lista=self.clientes.listar_cliente() # guardamos en la variable lista lo que retornamos
                # validamos
                if not lista:
                    print("No hay Clientes")
                    return
                else:
                    for clientes in lista:
                     print(f"ID: {clientes[0]}, NOMBRE: {clientes[1]}, TELEFONO: {clientes[2]}, EMAIL: {clientes[3]} ")



            elif opcionMenu =="3":
                print("Buscar Clientes ")

            
            elif opcionMenu =="4":
                print("Editar Clientes")

            elif opcionMenu =="5":
                print("eliminar Clientes ")


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

            elif opcionMenu =="2":
                print("Listar Ventas ")


            elif opcionMenu =="3":
                print("Buscar Ventas ")

            
            elif opcionMenu =="4":
                print("Editar Ventas")

            elif opcionMenu =="5":
                print("eliminar Ventas ")


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
                print("Ingresar ")

            elif opcionMenu =="2":
                print("Listar ")


            elif opcionMenu =="3":
                print("Buscar ")

            
            elif opcionMenu =="4":
                print("Editar ")

            elif opcionMenu =="5":
                print("eliminar ")


            elif opcionMenu =="6":
                print("Saliendo del menuCrud de ")
                break
            else:

                print("Opcion incorrecta")
if __name__ == "__main__":
    principal=Principal()
    principal.ejecutar_tablas()