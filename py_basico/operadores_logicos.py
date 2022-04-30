#and

print ("Conjunción (and)")

a= int(input("Escribe un numero mayor a 2 y menor que 5: "))

if a > 2 and a < 5:
    print ("El numero",a,"cumple con la condicion \n")

else:
    print ("El numero",a,"no cumple con la condicion \n")

#or

print ("Disyunción (or)")

b= input("Para cumplir la condicion escribe la palabra 'si' o 'yes': ")

b= b.lower ()

if b== "si" or b== "yes":
    print ("La condicion se cumplio \n")

else:
    print ("La condicion no se cumplio \n")


#not

print ("Negacion (not)")

c= int(input("Introduce un numero igual a 5: "))

if not c == 5:
           print ("El numero no es igual a 5 y la condicion se cumple")

else:
    print ("El numero es igual a 5 y no se cumple la condicion")




















