def mensaje():
    print("Hola")
    print("No repitas codigo")


mensaje()
mensaje()
mensaje()


def lineas(mensaje):
    print("Hola")
    print("mi nombre es Frailejon Hernesto Perez ")
    print("Has escogido la opcion", mensaje)
    print("adios te desea Frailejon Hernesto Perez ")


opcion = int(input("\nIngresa un numero del 1 al 3: "))

if opcion == 1:
    lineas("Elegiste la opcion 1")
elif opcion == 2:
    lineas("Elegiste la opcion 2")
elif opcion == 3:
    lineas("Elegiste la opcion 3")
else:
    print("Opcion Invalida")


def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado


sumatoria = suma(1, 4)
print(sumatoria)
