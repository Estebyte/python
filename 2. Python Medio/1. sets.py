"""
- Se pueden modificar
- No tienen orden
- No permiten duplicados
"""

my_set = {"col", 3, False, 8.9} #No es un diccionario
print (my_set)
print (type(my_set))

set_from_string = set("Hello")
print (set_from_string)

mytuple = (1, 3, 1, 5, 6, 3, 7, 9, 2, 4, 5, 6, 7, 8)
set_from_tuple = set(mytuple)
print (set_from_tuple)
