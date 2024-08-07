class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print("hola")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f"Mi habilidad mágica super especial es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa

    def mostrar_habilidad(self): #Aqui se esta accediendo y reescribiendo al metodo "mostrar_habilidad()" que ha heredado la subclase
        print("no tengo jaja") 

    def presentarse(self):
        print(f"Hola, soy {self.nombre}. {super().mostrar_habilidad()} y trabajo en {self.empresa}")
        # super().mostrar_habilidad() accede directamente al metodo de la superclase
    
    #Es una buena practica acceder directamente al metodo de la superclase para evitar problemas posteriores si se reescribe el mismo metodo en la subclase

# Crear una instancia de EmpleadoArtista
humano1 = EmpleadoArtista("Esteban", 17, "Colombiano", "tocar guitarra", 0, "Vagos S.A.S")

# Probar los métodos
humano1.presentarse()

#issubclass 
print(issubclass(EmpleadoArtista, Artista))

#isinstance
print(isinstance(humano1, Persona)) #humano1 tambien es una instacia de Persona y Artista, al ser EmpleadoArtista una subclase de estas dos