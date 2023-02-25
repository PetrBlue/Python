# Quadratic equation

import math

a = int(input("What value is a? "))
b = int(input("What value is b? "))
c = int(input("What value is c? "))
d = b * b - 4 * a * c
i = False
onlyOne = False
if(d < 0):
    i = True
if(d == 0):
    onlyOne = True
x1 = (-b + math.sqrt(abs(d))) / (2 * a) 
x2 = (-b - math.sqrt(abs(d))) / (2 * a)
if(onlyOne == True):
    print("The answer is " + str(x1) + ".")
if(i == True):
    print("The answers are: x1 = " + str(x1) + "i and x2 = " + str(x2) + "i.")
if(i == False and onlyOne == False):
    print("The answers are: x1 = " + str(x1) + " and x2 = " + str(x2) + ".")