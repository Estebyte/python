#Recreación de Math.random() de javascript

import random

def random_float(): 
    """
    Equivalente a la función Math.random() de javascript,
    que toma un numero aleatorio entre 0 y 1
    """
    x = random.uniform(0, 1)
    return(x)

def rand_num(min, max):
    return int(random_float() * (max - min + 1) + min) #Siendo int() equivalente a Math.floor()
    
   
min = int(input("Ingrese el minimo numero del rango: "))
max = int(input("Ingrese el maximo numero del rango: "))

print("El numero aleatorio es: ", rand_num(min, max))
