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

            elif opcionMenu =="2":
                print("Listar proveedores")


            elif opcionMenu =="3":
                print("Buscar proveedor")

            
            elif opcionMenu =="4":
                print("Editar Proveedor")

            elif opcionMenu =="5":
                print("eliminar proveedor")


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

            elif opcionMenu =="2":
                print("Listar Categoria")


            elif opcionMenu =="3":
                print("Buscar Categoria")

            
            elif opcionMenu =="4":
                print("Editar Categoria")

            elif opcionMenu =="5":
                print("eliminar Categoria")


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