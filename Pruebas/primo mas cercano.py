def run():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    number= int(input("Ingresa un numero del 1 al 100 para encontrar su numero primo siguiente: "))

    if number in prime_numbers:
        print("Este numero ya es primo")

    while not number in prime_numbers:
        number += 1
        if number in prime_numbers:
            print(number)
            break
        
if __name__ == "__main__":
    run()

