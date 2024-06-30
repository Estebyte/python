"""
my_dict = {}

for i in range(1, 5):
    my_dict[i] = i * 2

print(my_dict)

dict_2 = {i: i * 2 for i in range(1, 5)}
print(dict_2)
"""


import random

countries = ["col", "mex", "pe"]
"""
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)
"""
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

# Agregar una condición final

results = {country: population for (country, population) in population_v2.items() if population > 20}
print(results)

# Crear un diccionario desde dos listas con dict comprenhension

names = ["Santiago", "Camilo", "Juan"]
ages = [12, 45, 8]
"""
my_dict = dict(zip(names, ages)) #zip() para unir las listas
print(my_dict)
"""
dict_2 = {name: age for (name, age) in zip(names, ages)}
print(dict_2)





