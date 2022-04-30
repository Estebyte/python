def conversor(tipo_pesos, valor_dolar):
    peso = input("\nCuantos pesos " + tipo_pesos + " tienes?: ")
    peso = float(peso)
    dolares = peso/valor_dolar
    dolares = round(dolares, 2)
    print("Tienes", dolares, "dolares")


menu = """
Conversor de moneda:

1- Pesos Colombianos
2- Pesos Mexicanos
3- Pesos Argentinos

Eliga su opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("COP", 3779)
elif opcion == 2:
    conversor("MXN", 19.89)
elif opcion == 3:
    conversor("ARG", 111.12)
else:
    print("Opción no valida")
