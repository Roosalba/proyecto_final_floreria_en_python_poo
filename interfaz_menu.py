
from principal import Principal  # Conectamos con tu clase principal

class MenuInteractivo:
    def __init__(self):
        # Creamos una instancia de tu sistema original
        self.sistema = Principal()

    
    def iniciar(self):

        print("********************************************")
        print("     INICIANDO INTERFAZ OPTIMIZADA       ")
        print("********************************************")
        
        #EJECUTAMOS LAS TABLAS DEL PRINCIPAL   
        self.sistema.ejecutar_tablas()

if __name__ == "__main__":
    menu = MenuInteractivo()
    menu.iniciar()