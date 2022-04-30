def run():
    diccionario = {
        "Llave1": 1,
        "Llave2": 2,
        "Llave3": 3,
    }
    # print(diccionario["Llave1"])
    # print(diccionario["Llave2"])
    # print(diccionario["llave3"])

    poblacion = {
        "Argentina": 33333,
        "Bolivia": 77777,
        "Monolandia": 6666,
    }
    # print(poblacion["Monolandia"])

    # for pais in poblacion.values():
    #     print(pais)

    for pais, poblacion in poblacion.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")


if __name__ == "__main__":
    run()
