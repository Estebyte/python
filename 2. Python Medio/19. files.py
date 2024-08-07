file = open("text.txt", "r")

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt") == f = open("demofile.txt", "rt")
"""

#print(f.read()) Leer archivo completo
#print(file.readline()) Leer por lineas

for line in file:
    print(line)

file.close()

with open("text.txt") as file: #Cierra automaticamente el archivo
    for line in file:
        print(line)