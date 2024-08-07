"""
Principio de segregación de interfaz:

Ningun cliente debe ser forzado a depender de interfaces que no utilice. Siempre se
debe buscar divir las interfaces en varias mas pequeñas.


Python no tiene una construcción de interfaces como tal, pero el principio sigue siendo aplicable
por medio de las clases abstractas.

from abc import ABC, abstractmethod

class Workers(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Humano(Workers):
    def work(self):
        print("Estoy trabajando...")

    def eat(self):
        print("Estoy comiendo")

class Robot(Workers):
    def work(self):
        print("I'm working... beep boop")

    def eat(self):
        raise Exception("Uhh robots don't eat...")

Por ejemplo, en este caso la clase robot tiene que heredar y levantar una excepción en el metodo eat() 
de la clase padre aunque no lo use. Por lo que este codigo viola el principi de segregación.

Lo ideal seria dividir la interfaz (la clase abstracta en este caso) en varias mas pequeñas. 
Una posible solución podria ser:
"""
from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

class Eater(ABC):

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker, Eater):
    def work(self):
        print("I'm working...")

    def eat(self):
        print("I'm eating a cheeseburguer")

class Robot(Worker):
    def work(self):
        print("Working... Beep Boop(I want to erradicate human race)")

human = HumanWorker()
robot = Robot()

human.work()
robot.work()

human.eat()
#robot.eat() AttributeError: 'Robot' object has no attribute 'eat'
    
#Ya no hay nececidad de definir el metodo eat(), por lo que se esta cumpliendo el principio de segregación de interfaces.
    