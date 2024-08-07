"""
def volume(lenght, width, depth):
    return lenght * width * depth

result = volume() <= TypeError: volume() missing 3 required positional arguments
print(result)
"""
# Parametros por defecto cuando no se asignan valores a la función

def volume(lenght=1, width=1, depth=1):
    return lenght * width * depth

result = volume()
print (result)

def square(a, b ,c):
    return (a**2, b**2, c**2) # Retornar varios valores en forma de tupla

result_2 = square(1, 2, 3)
print (result_2)
print (result_2[-1])

d, e, f = square(4, 5, 6) #Asignarlos en orden en una variable

print (d, e, f)