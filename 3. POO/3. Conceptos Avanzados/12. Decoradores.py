"""
 Un decorador es una función que cambia el funcionamiento de otra, 
 agregandole funcionalidad antes o despues de ejecutarla. 
 Se llama con @
"""
def my_decorador(func):
    def new_func():
        print("Inició del programa:")
        func()
        print("Final del programa...")
    return new_func

"""
def saludar():
    print("Hola, mi nombre es Frailejón Ernesto Perez")

saludo_decorado = decorador(saludar)
saludo_decorado()
"""

@my_decorador
def saludo():
    print("Hola, mi nombre es Frailejón Ernesto Perez")

saludo()