i = 0

'''
while i < 10:
    i += 1
    print (i)
'''

"""
while i < 10:
    i += 1
    if i == 5:
        break #Para romper el ciclo forzadamente
    print (i)

"""

while i < 10:
    i += 1
    if i == 5:
        continue
    print (i)  #Este print nunca se ejecutara cuando i == 5