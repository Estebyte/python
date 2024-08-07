#Reduce a un solo valor

import functools

numbers = [1, 2, 3, 4]

def acummulator(counter, item):
    print("Counter =", counter)
    print("Item =", item)
    return counter + item


sum = functools.reduce(acummulator, numbers)
print(sum)