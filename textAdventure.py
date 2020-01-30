import random
import math
from time import sleep

def choice(question, options: list):
    print(question + " ")
    ans = input("/".join(options) + "? ")

    i=1
    for o in options:
        print("%")

    i = 0
    for o in options:
        if o in ans:
            return(ans)

        if keywords:
            for k in keywords[i].split(" "):
                if k in ans:
                    return(ans)

        i += 1

    choice(question, options)

print("Welcome to the planet of Krypton")
pname = input("What is your name? ")
print("Nice to meet you %s, my name is Clark" %(pname))
sleep(2)
print("I just found you in a pod an hour ago, do you know how you got here?")
sleep(3)
print("No?, you must be suffering through some sort of amnesia")
hplanet = choice("Do you know what planet you came from?", ["earth", "mars", "saturn"])
print(hplanet)
choice("Well what would you like to do?", ["Go Touring", ""])