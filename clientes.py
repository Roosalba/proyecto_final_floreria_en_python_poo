from database import Generico

class Cliente:
    def __init__(self,id_cliente,nombre,telefono,email):
        self.id_cliente=id_cliente
        self.nombre=nombre
        self.telefono=telefono
        self.email=email


objeto1=Cliente(1,'rosalba','123333','rosalba15@')

print(objeto1)
