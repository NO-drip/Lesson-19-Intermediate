import random

while True:
    user_choice = input("Choose wisely between Rock, paper or scissors!")
    possible = ["rock","paper","scissors"]
    computer_choice = random.choice(possible)
    if user_choice == computer_choice:
        print ("It is a tie")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else: print("You lose!")
    elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
            else: print("You lose!")
    elif user_choice == "scissors":
            if computer_choice == "rock":
                print("You win!")
            else: print("You lose!")
    go = input("Do you want to go again?")
    if go == "no":
        break
        