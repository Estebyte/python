'''
for i in range(5, 11):
    print (i)
'''

my_list = [3,5,6,5]
for i in my_list:
    print (i)

my_tuple = (2,1,"Juan")
for i in my_tuple:
    print (i)

my_dict = {
    "name": "zapato",
    "price" : 2,
    "stock": 4
}

print (my_dict.items())
for key, values in my_dict.items():
    print (key, ": ",values)


people = [
    {
        "name" : "esteban",
        "age" : 17
    },
    {
        "name" : "tobias",
        "age" : 99,
    },
    {
        "name" : "juanito",
        "age" : 3,
    }
]

for person in people:
    print (person)
for person in people:
    print ("name => ", person["name"])