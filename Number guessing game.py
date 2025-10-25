import time

import random

import winsound

for x in range(2):

 winsound.Beep(1000, 500)



print("Welcome to the Number Guessing Game!")

time.sleep(1)

print("Here you guess numbers between 1 and 10 with 3 attempts.")

time.sleep(0.5)

print("Let's begin!")

random_num = random.randint(1, 10)

for x in range(3):


    guess = int(input("Enter your guess: "))

    if guess < random_num:

        print("Too low!")

    elif guess > random_num:

        print("Too high!")

    else:

        print("Congratulations! You've guessed the number!")

        break