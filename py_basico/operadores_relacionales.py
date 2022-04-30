print("introduce 2 numeros a comparar: \n")

num1 = int(input("Introduce el numero 1: "))
num2 = int(input("Introduce el numero 2: "))

print ("\nLos numeros a comparar son:",num1 ,"y" ,num2, "\n")

if num1 < num2:
    print (num1,"es menor que",num2)

if num1 > num2:
    print (num1,"es mayor que",num2)

if num1 == num2:
    print (num1,"es igual que",num2)

if num1 != num2:
    print (num1,"no es igual a",num2)

if num1 <= num2:
    print (num1,"es menor o igual que",num2)

if num1 >= num2:
    print (num1,"es mayor o igual que",num2)
