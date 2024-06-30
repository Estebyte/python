"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

w+ => Permisos tanto de lectura como de escritura. Enfocado en reescribir
r+ => Permisos tanto de lectura como de escritura. Enfocado en agregar
"""

# Abriendo un archivo para escritura y lectura ('w+')
with open('./24_text.txt', 'w+', encoding="utf-8") as file:
    # Escribir en el archivo
    file.write("Nuevas cosas en este archivo\n")
    file.write("Hola\n")
    file.write("Holaaaaá\n")

    # Regresar al inicio del archivo para leer
    file.seek(0)

    # Leer el contenido del archivo
    for line in file:
        print(line)