import random


def run():
    numero_aleatorio = random.randint(1, 100)
    intentos = 6
    print("\nIntenta adivinar un numero del 1 al 100. Tienes 6 intentos")
    while True:
        numero_elegido = int(
            input("\nEscribe tu numero: "))

        if numero_elegido < numero_aleatorio and intentos > 1:
            intentos -= 1
            print(
                f"\nEl numero secreto es mas grande. Te quedan {intentos} intentos")

        elif numero_elegido > numero_aleatorio and intentos > 1:
            intentos -= 1
            print(
                f"\nEl numero secreto es mas pequeño. Te quedan {intentos} intentos")

        elif numero_elegido == numero_aleatorio:
            print("\nFelicidades :D, Adivinaste el numero")
            break

        else:
            print("\nPerdiste :c")
            break


if __name__ == "__main__":
    run()
