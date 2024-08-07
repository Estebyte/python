"""
Principio de substitución de Liskov:
Las subclases deben ser sustituibles por sus superclases, es decir:
class A(B) ==> Donde sea que se use B, tambien deberia poder usarse A.

Asi al crear una subclase, esta no deberia cambiar el comportamiento de la superclase.
"""
"""
class Animal:
    def walk(self):
        print("Walking...")

    def jump(self):
        print("Jumping...")
        
def jumphole(a = Animal): #variable de parametro
    a.walk()
    a.jump()
    a.walk()

class Elephant(Animal):
    def jump(self):
        raise Exception("I can't jump...")
    
jumphole(Elephant())

#El codigo incumple el principio de liskov, porque la clase Elephant no puede realizar el metodo jump de su #superclase Animal. 

#La abstracción escodiga no es la correcta, seria mejor:
"""
class Animal():
    def walk(self):
        print("Walking...")

class LightWeightAnimal(Animal):
    def jump(self):
        print("Jumping")

def jump_hole(a = LightWeightAnimal):
    a.walk()
    a.jump()
    a.walk()

class Elephant(Animal):
    pass
class Dog(LightWeightAnimal):
    pass

#Probar la función jump_hole:
jump_hole(Dog())
#jump_hole(Elephant()) => AttributeError: 'Elephant' object has no attribute 'jump'

"""
Ahora clase elefante puede cumplir las mismas funciones que la clase animal, 
ya que el metodo jump_hole solo recibe como parametro a la subclase LightWeightAnimal.
La solución, respeta el principio de sustitución de Liskov
"""