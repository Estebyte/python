"""
Exception Description

try: Permite probar un bloque de código en búsqueda de un error.

except: Permite manejar el tipo de error en el bloque.

else :Permite ejecutar el código cuando no hay ningún tipo de error en el bloque.

finally :Permite ejecutar el código en el bloque, 
independiente en el resultado de los bloques de prueba y excepción
"""

def pruebas():
    print (0 / 0) #Se corta el script
    print ("Hola") 

def zerodivision(a, b):
   try:
      result = a / b
   except ZeroDivisionError:
      return "No se puede dividir por 0"

   return result

def pruebas3(x, y):
    try:
        assert x == y, "Los numeros deben ser iguales"
    except AssertionError as error:
        print(error)

    print("Hola")

def just_even(x):
    try:
       assert x % 2 == 0, "The number must be even"
    except AssertionError as error:
        print(error)
    else:
        print(True) #Pass para no hacer nada
    finally:
        print("End of the script (and the world)")

def valid_age(age):
    try:
        assert type(age) is int, "Enter a valid number"
        if age < 18:
            raise Exception("No minors allowed")
        
    except Exception as error:
        print(error)
    
    except AssertionError as error:
        print(error)
    
    else:
        print("Your age is valid")

    finally:
        print("Thanks for using our services!")

print(zerodivision(10, 2))
print(zerodivision(10, 0))