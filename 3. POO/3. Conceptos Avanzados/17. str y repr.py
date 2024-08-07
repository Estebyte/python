#O tambien metodos duner
class Persona:
    def __init__(self, name, age): #Metodo constructor (Construye al objeto)
        self.name = name
        self.age = age

    def __str__(self): #Retorna el objeto en un string, lo que permite imprimirlo directamente
        return f"Name ==> {self.name}\nAge ==> {self.age}"
    """
    La función interna de python str(), print() y format () llama a este mismo metodo.
    Y cuando __str__ no esta definida, las funciones internas acuden al __repr__ predefinido
    por Python.
    """

    def __repr__(self): #Permite hacer una representación del objeto mas completa que str()
        return f'Persona("{self.name}", {self.age})'


yo = Persona("Esteban", 17)
print(yo)

representacion = repr(yo)
print(representacion)

#De una representación, tambien se puede crear una reconstrucción del objeto con eval()
reconstruccion_yo = eval(representacion)
print(f"Objeto Reconstruido desde una representación:\n{reconstruccion_yo}")

print(yo == reconstruccion_yo)