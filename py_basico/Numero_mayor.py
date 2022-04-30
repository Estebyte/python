print("====================")
print("El numero mas grande")
print("====================\n")


a= int(input("Escribe un numero: "))
b= int(input("Escribe un numero: "))
c= int(input("Escribe un numero: "))

if a > b and a > c :
    print ("El numero",a,"es el mayor")

elif b > c and b > a :
    print ("El numero",b,"es el mayor")

elif c > a and c > b :
    print ("El numero",c,"es el mayor")

