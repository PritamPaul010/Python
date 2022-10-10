import random


def game():
    rand_num = random.randint(1,100)
    a = []
    for i in range (1,100): 
        user_input = input("Enter your number (1-100):\n")
        if user_input==" ":
            print (f"The number is: {rand_num}")
            break
        else: 
            user_input_int = int(user_input)
            if user_input_int == rand_num:
                print (f"Congrats! You have guessed the right number. Attempts made: {len(a)+1}")
                break
            elif user_input_int<rand_num:
                print (f"Try higher. It is less than the number. (To know the number press 'Space bar')")
                a.append(user_input_int)
            else:
                print (f"Try lower. It is higher than the number. (To know the number press 'Space bar')")
                a.append(user_input_int)
for i in range(1,60):
    print("Welcome to 'Guess the Number' Game.")
    for i in range(1,60):
        main_input = input("Please, press '0' to start the Game.\n")
        if main_input == '0':
            game()
            print (f"Would you like to play one more round? (Press '+' to continue or press '-' to exit.)")
            continue_or_exit = input()
            for i in range(1,60):
                if continue_or_exit == '-':
                    break
                elif continue_or_exit == '+':
                    game()
                else: 
                    print("Wrong key pressed. (Press '+' to continue or press '-' to exit.)")#Only showing one time 
            break
        else: 
            print("Wrong key pressed.")
    break
