def run():
    LIMIT = 1000
    cont = 0
    cube = 2**cont

    while cube < LIMIT:
        print(f"2 elevado a {cont} es igual a {cube}")
        cont = cont + 1
        cube = 2**cont


if __name__ == "__main__":
    run()
