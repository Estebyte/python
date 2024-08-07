price = 100 #Alcance global

def inversion():
    price += 10 #Alcance local, diferente a price global
    print(price)

print(price)

"""
inversion() => UnboundLocalError: cannot access local variable 'price' where it is not associated with a value
"""
