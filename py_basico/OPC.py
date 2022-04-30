print ("=========")
print ("Conversor")
print ("=========\n")


print ("Menu de Opciones: \n")
print ("Presiona 1 para convertir de numero a palabra")
print ("Presiona 2 para convertir de palabra a numero")

opcion = int (input("Seleciona tu opcion:"))

if opcion == 1:
    print ("\n Conversor de numero a palabra \n")

    opcion_uno = int (input("Que numero desea convertir: "))

    if opcion_uno == 1:
        print ("El numero es 'Uno'")
    elif opcion_uno == 2:
        print ("El numero es 'Dos'")
    elif opcion_uno == 3:
        print ("El numero es 'Tres'")
    elif opcion_uno == 4:
        print ("El numero es 'Cuatro'")
    elif opcion_uno == 5:
        print ("El numero es 'Cinco'")
    else:
        print ("El numero",opcion_uno,"no esta registrado")
        

elif opcion == 2:
    print ("\n Conversor de palabra a numero \n")

    opcion_dos = input("Que palabra desea convertir: ")
    opcion_dos = opcion_dos.lower ()

    if opcion_dos == "uno":
        print ("El numero es '1'")
    elif opcion_dos == "dos":
        print ("El numero es '2'")
        
    elif opcion_dos == "tres":
        print ("El numero es '3'")
    elif opcion_dos == "cuatro":
        print ("El numero es '4'")
    elif opcion_dos == "cinco":
        print ("El numero es '5'")
    else:
        print ("La palabra",opcion_dos,"no esta registrada")

else:
    print ("Opcion no disponible")



