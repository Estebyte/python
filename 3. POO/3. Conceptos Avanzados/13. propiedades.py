class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property #==> Decorador especial para getters
    def name(self): #==> Getter
        return self.__nombre
    
    @name.setter #==> Decorador especial para setters
    def name(self, nuevo_nombre): #==> Setter
        self.__nombre = nuevo_nombre
    
    @name.deleter #Para eliminar el atributo despues de usarlo, sin modificar el atributo original
    def name(self):
        del self.__nombre
        
yo = Persona("Esteban", "17")

#Probar el getter
mi_nombre = yo.name 
#Permite tratar a la función como un atributo y no un metodo. Haciendolo mas limpio y escalable
print(mi_nombre)

#Probar el setter
yo.name = "Juan"
mi_nombre = yo.name 
print(mi_nombre)

#Probar el deleter
del yo.name
#mi_nombre = yo.name ==> AttributeError: 'Persona' object has no attribute '_Persona__nombre'

#De esta manera, encapsulamos las propiedades ocultas de una forma mas limpia
