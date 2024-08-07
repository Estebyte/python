"""
En Python todo es un objeto de una clase, y cada objeto tiene metodos especiales 
que utiliza para interactuar con otros objetos.

Por ejemplo el numero 1 y el numero 2 son objetos de la clase int, y python define automaticamente
los metodos especiales con representados con operadores para que estos puedan interactuar entre si:

1 + 2 = 3

De la misma forma, tambien podemos sobrecargar estos metodos especiales en nuestras clases para 
definir la interacción entre sus objetos.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        nueva_edad = self.edad + other.edad
        return Persona(self.nombre + " " + other.nombre, nueva_edad)
    
    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"
    
juan = Persona("Juan", 3)
camilo = Persona("Camilo", 10)
nueva_persona = juan + camilo

print(nueva_persona)