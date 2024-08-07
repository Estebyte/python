""""
 Get ==> Obtener
 Set ==> Modificar
"""
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self): #==> Getter
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre): #==> Setter
        self.__nombre = nuevo_nombre
        
yo = Persona("Esteban", "17")
mi_nombre = yo.get_nombre()
print(mi_nombre)

yo.set_nombre("Juan")
mi_nombre = yo.get_nombre()
print(mi_nombre)
