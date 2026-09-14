import random
gaming = True
number = str(random.randint(0,10))
print ("Welcome to the guessing game. I will randomly select a number between 1 to 9.")
print ("The objective of this game is to guess the number and be the number hero.")
while True:
    guess = input("Please enter a number to guess.")
    if guess == number:
        print("Well done! You have cracked the random number!")
        break
    else:
        print(f"The number {guess} is incorrect. Try again.")