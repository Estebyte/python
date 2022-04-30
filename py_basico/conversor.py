# Conversor de moneda pa
print("\nConversor de moneda \n")

print("Opcion 1: Dolares a COP")
print("Opcion 2: COP a Dolares \n")

opcion = int(input("Elija su opcion: "))

if opcion == 1:
    dolares = input("Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso = 0.00026
    peso = dolares/valor_peso
    peso = round(peso, 2)
    print("Tienes", peso, "pesos")

elif opcion == 2:
    peso = input("Cuantos pesos COP tienes?: ")
    peso = float(peso)
    valor_dolar = 3779
    dolares = peso/valor_dolar
    dolares = round(dolares, 2)
    print("Tienes", dolares, "dolares")


else:
    print("Opción no valida")
