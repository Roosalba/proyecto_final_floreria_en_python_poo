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
                
                
            elif opcion_tabla =="2":
                print("Ingresate a la tabla Categoria ")


            elif opcion_tabla =="3":
               print("Ingresate a la tabla Articulos ")



            elif opcion_tabla =="4":
                print("Ingresate a la tabla Metodo_pago ")



            elif opcion_tabla =="5":
                print("Ingresate a la tabla Clientes ")


            elif opcion_tabla =="6":
                 print("Ingresate a la tabla Ventas ")



            elif opcion_tabla =="7":
                 print("Ingresate a la tabla Detalle_ventas ")


            


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
    def 