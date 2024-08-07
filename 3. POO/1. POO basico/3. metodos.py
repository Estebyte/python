#Todas las funciones dentro de una clase, son metodos.

class Celular:
    def __init__(self, marca, modelo, camara):
        #__init__ es un metodo constructor en el que se definen las propiedades inciales del objeto.
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"Estas llamando desde tu {self.modelo}")

    def colgar(self):
        print(f"Estas colgando desde tu {self.modelo}")

celular1 = Celular("Samsung", "S23", "48MP")
celular1.llamar()
celular1.colgar()

celular2 = Celular("Apple", "Iphone 15", "38MP")
celular2.llamar()
celular2.colgar()