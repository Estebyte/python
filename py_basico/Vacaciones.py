print("=======================")
print("Calculador de Vcaciones")
print("=======================\n")

name = input("Introduzca su nombre: ")
clase = int(input("Introduzca su clase: "))
años = float(input("Introduzca sus años en la empresa: "))


if clase == 1:
    if años >= 1 and años < 2:
        print (name,",tienes derecho a 6 días")

    elif años >= 2 and años <= 6:
        print (name,",tienes derecho a 14 días")

    elif años >= 7:
        print (name,",tienes derecho a 20 días")

    else:
        print (name,",no tienes derecho a vacaciones")

elif clase == 2:
    if años >= 1 and años < 2:
        print (name,",tienes derecho a 6 días")

    elif años >= 2 and años <= 6:
        print (name,",tienes derecho a 15 días")

    elif años >= 7:
        print (name,",tienes derecho a 22 días")

    else:
        print (name,",no tienes derecho a vacaciones")
    
elif clase == 3:
    if años >= 1 and años < 2:
        print (name,",tienes derecho a 10 días")

    elif años >= 2 and años <= 6:
        print (name,",tienes derecho a 20 días")

    elif años >= 7:
        print (name,",tienes derecho a 30 días")

    else:
        print (name,",no tienes derecho a vacaciones")

else:
    print ("Esa clase no existe")
