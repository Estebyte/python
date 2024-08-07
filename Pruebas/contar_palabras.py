def contar_palabras(palabra):
    lista_palabras = palabra.split()
    return len(lista_palabras)

mifrase = contar_palabras("Hola, Mi nombre es frailejon Ernesto Perez")
print(mifrase)