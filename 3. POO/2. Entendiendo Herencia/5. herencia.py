#Herencia simple
class Persona: #CLase Padre/Superclase
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def bailar(self):
        print("Bailandooo, bailandoooo...")

class Empleado(Persona): #Clase Hija/Subclase
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): #Tambien hay que dar como parametros los atributos de la clase padre
        super().__init__(nombre, edad, nacionalidad) #En esta linea se definen los atributos a heredar de la clase padre con el metodo super()
        self.trabajo = trabajo
        self.salario = salario

#Tambien existe el concepto de herencia jerárquica, donde hay varias subclases que dependen de una superclase
        
empleado1 = Empleado("Juan", 13, "peruano", "minero", 0) 
empleado1.bailar()
print(empleado1.salario)