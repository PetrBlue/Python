# Password generator

import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = ".-,?:_!/*+|"

passwordLength = int(input("How many characters? "))

password = ""

while(passwordLength > 0):
    rnd = random.randint(0, 3)
    if(rnd == 0):
        rndLowercase = random.randint(0, 25)
        password += lowercase[rndLowercase]
    if(rnd == 1):
        rndUppercase = random.randint(0, 25)
        password += uppercase[rndUppercase]
    if(rnd == 2):
        rndNumbers = random.randint(0, 9)
        password += numbers[rndNumbers]
    if(rnd == 3):
        rndSymbol = random.randint(0, 9)
        password += symbols[rndSymbol]

    passwordLength -= 1

print("Your generated password: " + password)