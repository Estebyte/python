#Create, Read, Update and Delete (CRUD)

nums = [1,2,3,4,5] 

nums.append(8) #Agregar al final

print (nums)

nums.insert(0, "America ya") #Insertar en una posición especifica

print (nums)

nums.remove("America ya")

print(nums)

list_1 = ["Who", "Can", "It"]
list_2 = ["be", "now"]

new_list = list_1 + list_2

print (new_list)

print (new_list.index("Who")) #Posición

new_list.pop()  #Elimina una posición especifica, o el ultimo elemento si esta no se indica
print(new_list)

new_list.pop(0)
print (new_list)

new_list.reverse() #Dar vuelta a la lista

print(new_list)

numbers = [3,4,2,87,6,47,257,425,86,1]

numbers.sort() #Ordenar de mayor a menor

print (numbers)

new_list.sort()

print (new_list) #Tambien ordena strings en orden alfabetico

#sort.() no funciona con una lista de tipos de datos diferentes

