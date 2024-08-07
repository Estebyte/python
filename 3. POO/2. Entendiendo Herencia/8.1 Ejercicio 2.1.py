class Animal:
    def comer(self):
        print("Comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando...")

class Ave(Animal):
    def volar(self):
        print("Volando...")

class Murcielago(Mamifero, Ave):
    def comer(self):
        print("El murcielago esta comiendo...")
    def amamantar(self):
        print("El murcielago esta amamantando...")
    def volar(self):
        print("El murcielago esta volando...")


#Crear intancia
mi_murcielago = Murcielago()

#Probar Metodos
mi_murcielago.amamantar()
mi_murcielago.comer()
mi_murcielago.volar()

#Acceder a los metodos de las superclases
Animal.comer(mi_murcielago)
Mamifero.amamantar(mi_murcielago)
Ave.volar(mi_murcielago)