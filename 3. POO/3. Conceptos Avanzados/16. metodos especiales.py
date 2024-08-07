#Metodos especiales o metodos dunner. Tienen su definición reservada por dos "_" al inicio y al final
class Persona:
    def __init__(self, name, age): #Metodo constructor (Construye al objeto)
        self.name = name
        self.age = age

    def __str__(self): #Retorna el objeto en un string, lo que permite imprimirlo directamente
        return f"Name ==> {self.name}\nAge ==> {self.age}"
        #La función interna de python str() llama a este mismo metodo

    def __repr__(self): #Permite hacer una representación del objeto mas completa que str()
        return f'Persona("{self.name}", {self.age})'

    
yo = Persona("Esteban", 17)
print(yo)

representacion = repr(yo)
print(representacion)
