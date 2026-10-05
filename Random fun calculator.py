import random
import math

print("=====WELCOME TO THE RANDOM FUN CALCULATOR!=====")

lucky = random.randint(1,10)
print (f"The lucky number is {lucky}")

lucky_activity = ["Number guessing.", "Reading books.", "Solve a puzzle.", "Sport.", "Video Games."]
random_activity_chosen = random.choice(lucky_activity)
print(f"The activity for today is:{random_activity_chosen}\n")
print ("\nThere's a secret number!\n Try to guess it.")
secret_number = random.randint(1,5)

while True:
    user_number = int(input("\nGuess a random number from 1 to 5!"))
    if user_number == secret_number:
        print ("UGH! YOU GUESSED THE LUCKY NUMBER!")
        break
    else:
        print ("HAHA! YOU LOST! TRY AGAIN")

decimal_number = float(input("Please enter a decimal number!"))

print (f"The ceiling value of {decimal_number} is:",math.ceil(decimal_number))
print (f"The floor value of {decimal_number} is:", math.floor(decimal_number))

a = 37
c = 42
print ("The copysign is:", math.copysign(a,c))

gcd_number = int(input("Enter a negative number."))
print (f"\nThe absolute value of {gcd_number} is:",math.gcd(gcd_number))

num_1 = int(input("Please enter a number."))
num_2 = int(input("Please enter another number."))
print(f"The GCD of {num_1} and {num_2} is:",math.gcd(num_1,num_2))





    






