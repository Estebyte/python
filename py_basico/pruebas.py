def run():
    numero = int(input("Escribe un numero: "))
    resultado = 2 ** (numero - 1)
    if resultado % numero == 1 or numero == 2:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()
