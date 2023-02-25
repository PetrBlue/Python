# Guess the number


import random

x = int(input("The lowest number? "))
y = int(input("The highest number? "))

number = random.randint(x, y)

userInput = int(input("Your guess? "))

while(number != userInput):
    if(userInput > number):
        userInput = int(input("Lower. Your next guess? "))
    if(userInput < number):
        userInput = int(input("Higher. Your next guess? "))

print("Well done! You win!")