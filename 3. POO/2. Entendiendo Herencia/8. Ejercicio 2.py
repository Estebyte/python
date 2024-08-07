class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Nombre ==> {self.nombre}") 
        print(f"Edad ==> {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) #No hay que añadir self al metodo super()
        self.grado = grado

    def imprimir_grado(self):
        print(f"El grado del estudiante es: {self.grado}")


estudiante1 = Estudiante("Juan", 12, "6to")
estudiante1.presentarse()
estudiante1.imprimir_grado()