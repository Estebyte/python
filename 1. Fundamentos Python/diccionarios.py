my_dict = {
    "avion": "medio de transporte",
    "usuario" : "Esteban",
    "apellido" : "Loaiza",
    "Edad" : 17,
}

print (my_dict)
print (len(my_dict))

print (my_dict["Edad"])

print (my_dict.get("avion"))

print (my_dict.get("lol")) #.get() retorna "None" si el valor no existe

print ("avion" in my_dict)