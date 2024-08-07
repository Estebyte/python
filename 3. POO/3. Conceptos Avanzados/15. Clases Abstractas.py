#Clase focalizada en crear otras clases. No se instancian.
from abc import ABC, abstractmethod #Importaciones necesarias

class Animal(ABC):
    @abstractmethod #Hacer el metodo abstracto, obliga a importarlo y definirlo en las subclases
    def talk(self):
        pass

class Duck(Animal):
    def talk(self):
        print("Quack!")

class Cat(Animal):
    pass
    def talk(self):
        print("Meow!")

#Probar las 2 subclases
my_duck = Duck()
my_cat = Cat()

my_duck.talk()
my_cat.talk()

#Probar instanciar la clase abstracta
try:
    my_animal = Animal()
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'talk'
except TypeError:
    print("No puedes crear una instancia de una clase abstracta!")
