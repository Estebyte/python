import random

options = ("piedra", "papel", "tijera")

rounds = 1

computer_wins = 0
user_wins = 0


while True:
    print ("*" * 10)
    print ("Round => ", rounds)
    print ("User wins =>",user_wins)
    print ("Computer wins =>", computer_wins)

    user_option = input("piedra, papel O tijera? ").lower().strip()
    computer_option = random.choice(options)
    

    if not user_option in options:
        print ("Elige una opción valida")
        continue
        
    else:
        print ("User option:", user_option)
        print ("Computer option:", computer_option)


    if user_option == computer_option:
        print("Es un empate!")

    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana tijera!")
            print("User wins")
            user_wins += 1
        else:
            print("papel gana a piedra")
            print("Computer wins")
            computer_wins += 1

    elif user_option == "papel":
        if computer_option == "tijera":
            print("Tijera gana a papel!")
            print("Computer wins")
            computer_wins += 1
        else:
            print("papel gana a piedra")
            print("User Wins")
            user_wins += 1

    elif user_option == "tijera":
        if computer_option == "piedra":
            print("piedra gana tijera!")
            print("Computer wins")
            computer_wins += 1
        else:
            print("tijera gana a papel")
            print("Usuario wins")
            user_wins += 1

    if computer_wins == 2:
        print ("Computer is the winner")
        break
    if user_wins == 2:
        print ("User is the winner")
        break

    rounds += 1
