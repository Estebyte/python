print("====================")
print("Teorema de Pitagoras")
print("====================\n")

print("ELIGA UNA OPCION\n")
print("1: Hallar la hipotenusa")
print("2: Hallar un cateto\n")

opcion = int(input())

if opcion == 1:
    a = int(input("Ingrese el cateto a: "))
    b = int(input("Ingrese el cateto b: "))
    h = (a**2 + b**2)**0.5
    print("La hipotenusa es: ", round(h))


elif opcion == 2:
    a = int(input("Ingrese la hipotenusa : "))
    b = int(input("Ingrese el cateto b: "))
    h = (a**2 - b**2)**0.5
    print("El cateto a es igual a:", round(h))

else:
    print("\n Opcion No Disponible")
