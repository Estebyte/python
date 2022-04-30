# def run():
#     # for contador in range(1000):
#     #     if contador % 2 != 0:
#     #         continue
#     #     print(contador)

#     # for i in range(10000):
#     #     print(i)
#     #     if i == 5678:
#     #         break

#     texto = input('Escribe un texto: ')
#     for letra in texto:
#         if letra == 'o':
#             break
#         print(letra)


# if __name__ == '__main__':
#     run()

def run():
    menu = """
Adivina un numero del 1 al 10. Tienes 3 intentos:

Ingresa tu numero: """

    intentos = 0

    while True:
        numero = int(input(menu))
        if numero != 7:
            print("\nEse no es, sigue intentando\n")
            intentos += 1

        else:
            print("\nAsi es, el numero del bicho siuuuuuu")
            break

        if intentos == 3:
            print("Se te acabaron los intentos")
            break


if __name__ == "__main__":
    run()
