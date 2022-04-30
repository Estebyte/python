menu = """
Conversor de moneda:

1- Pesos Colombianos
2- Pesos Mexicanos
3- Pesos Argentinos

Eliga su opción: """
opcion = int(input(menu))

if opcion == 1:
    peso = input("Cuantos pesos COP tienes?: ")
    peso = float(peso)
    valor_dolar = 3779
    dolares = peso/valor_dolar
    dolares = round(dolares, 2)
    print("Tienes", dolares, "dolares")

elif opcion == 2:
    peso = input("Cuantos pesos MEX tienes?: ")
    peso = float(peso)
    valor_dolar = 19.86
    dolares = peso/valor_dolar
    dolares = round(dolares, 2)
    print("Tienes", dolares, "dolares")

elif opcion == 3:
    peso = input("Cuantos pesos ARG tienes?: ")
    peso = float(peso)
    valor_dolar = 111.21
    dolares = peso/valor_dolar
    dolares = round(dolares, 2)
    print("Tienes", dolares, "dolares")

else:
    print("Opción no valida")
