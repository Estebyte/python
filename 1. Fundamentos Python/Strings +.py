text = " Buenas Tardes Compatriotas"
print ("Hello" in text) # Está en? T/F

if "Buenas Tardes" in text:
    print ("Buenas Tardes Capitan")

size = len(text) #Tamaño en caracteres totales del texto

print (size)


print (text.lower()) 
print (text.upper())
print (text.swapcase()) 

print (text.strip()) #Elimina espacios al inicio y final

print (text.count("a")) 

print (text.startswith("lol")) # Empieza con? T/F
print (text.endswith("Compatriotas"))

print (text.replace("Compatriotas", "Mi gente latino")) 



text_2 = "este es un titulo"

print (text_2)

print (text_2.capitalize()) #La primera letra de la primera palabra en mayuscula
print (text_2.title()) #La primera letra de cada palabra en mayuscula

print (text_2.isdigit()) #Es un digito? T/F