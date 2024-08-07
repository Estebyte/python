person = {
    "name": "Esteban",
    "last_name" : "Loaiza",
    "age" : 17,
    "instruments" : ["Guitar", "Piano"],
    "Humano" : True,
}

print (person)

person["name"] = "Elsa Pato"

person["age"] -= 5

person["instruments"].append("Bass")

del person ["last_name"]

person.pop ("Humano")

print (person)

print ("Items:", person.items())

print ("Keys:", person.keys())

"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""