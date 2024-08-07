#Mismo metodo, diferentes resultados
class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"
  
don_gato = Gato()
manchas = Perro()

print(don_gato.sonido())
print(manchas.sonido())

#O tambien:

def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(don_gato)
hacer_sonido(manchas)