import random
import os
import time

def error(error_var): 

    if error_var.isalnum() == True and len(error_var) == 1:
        try:
            error_var = int(error_var)

            if error_var * 1 == error_var:
                return True
        except ValueError:
            return False

    else:
        raise ValueError("Oops... Solo puedes ingresar una letra")


def run():
    with open("Python\Pruebas\data.txt", "r", encoding="utf-8") as f:
        palabras = [line for line in f]

    os.system("clear")

    palabra_base = random.choice(palabras)

    a,b = 'áéíóúü','aeiouu'        
    trans = str.maketrans(a,b)                           #Sistema de normalizacion de las tildes
    palabra= palabra_base.translate(trans).upper()

    len_palabra = int(len(palabra))               
    os.system("clear") 

    rayas = ["_" for i in range (1,len_palabra)] 
    intentos = len_palabra + len_palabra//2     

    while True:
        try:
            print("¡Adivina la palabra!  Tienes",intentos,"intentos")
            print(' '.join(rayas)) 

            letra = input("\nIngresa una letra: ").upper()

            if error(letra) == True:
                raise ValueError("Oops... Solo puedes ingresar una letra")

            for index, value in enumerate(palabra):
            
                if value == letra:
                    rayas[index] = letra
                    os.system("clear")
                    intentos += 1

                else: 
                    os.system("clear")

            a= rayas.count(letra) 
            if a > 1:
                intentos -= a - 1

            if "_" in rayas:
                intentos -= 1

            if not "_" in rayas:
                os.system("clear") 
                print("Ganaste... La palabra es",palabra_base)


                opcion = int(input("\nSelecciona 1 para seguir jugando, 2 para salir: "))

                if opcion == 1:
                    os.system("clear")
                    palabra_base = random.choice(palabras)
                    a,b = 'áéíóúü','aeiouu'        
                    trans = str.maketrans(a,b)                           
                    palabra= palabra_base.translate(trans).upper()   
                    len_palabra = int(len(palabra))               
                    os.system("clear")             
                    rayas = ["_" for i in range (1,len_palabra)] 
                    intentos = len_palabra + len_palabra//2 

                elif opcion == 2:
                    os.system("clear")
                    break 
            
            if intentos == 0:
                os.system("clear") 
                print("Perdiste :c ... La palabra era",palabra_base)
                
                opcion = int(input("\nSelecciona 1 para seguir jugando, 2 para salir: "))

                if opcion == 1:
                    os.system("clear")
                    palabra_base = random.choice(palabras)
                    a,b = 'áéíóúü','aeiouu'        
                    trans = str.maketrans(a,b)                           
                    palabra= palabra_base.translate(trans).upper()   
                    len_palabra = int(len(palabra))               
                    os.system("clear")             
                    rayas = ["_" for i in range (1,len_palabra)] 
                    intentos = len_palabra + len_palabra//2 

                elif opcion == 2:
                    os.system("clear")
                    break 

        except ValueError as ve:
            os.system("clear")
            print (ve)
            time.sleep(2)
            os.system("clear")


if __name__ == "__main__":
    run()