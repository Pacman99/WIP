"""
b=True
d=False
print(b and d)
print(b or d)
print(not(d))

#h = input("What is your name?")
if(a == 'yes'):
    print("Now this will happen")
elif(a != 'no'):
    print("Aw, why would you do that?")
else:
    print("please answer yes or no")

h = "hellofsd"

l = ["jksd", 8, "klsd", True]

print(l)

f = "John"
l = "Doe"
f += " Doe"
print(f[-1])

#ans = input("So your name is %s , correct?" %(f))

from math import *
print(sqrt(49))

b=3
h=4
print(.5*b*h)
#OR
print((b*h)/2)
#OR EVEN
print(b/2*h)

colors = ["red", "blue", "orange", "purple", "white"]
colors.append("violet")
colors[-1] = "black"
del(colors[2])

print(colors[2])

print(["red"] * 4)

b=3
h=4
print(.5*b*h)
#OR
print((b*h)/2)
#OR EVEN
print(b/2*h)
for color in colors:
    if color == "green":
        print("Its a leaf")
    print(color)
def fizzBuzz():
    for i in range(1,101):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizz buzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)
fizzBuzz()
fizzbuzz()

def triangle(b,h):
    return(.5*b*h)


from apcs import *

Window.size(500,500)
Window.out.background("white")
#x = 0
color = "red"

def main():
    #global x
    global color
    x = Window.mouse.getX()
    y = Window.mouse.getY()
    if Window.mouse.clicked():
        if x >= 90 and x <= 110 and y >= 90 and x <= 110:
            color = "green"


    Window.out.color(color)
    Window.out.rectangle(100,100,20,20)

Window.frame(main)
Window.start()

p = [24,234,234,11]
print(p)
p[2] += 1000
print(p)

from tkinter import *
def keyup(e):
    print('up', e.char)
def keydown(e):
    print('down', e.char)

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()
"""
from apcs import *

Window.size(500,500)
Window.out.background("white")

def main():
    rect = Window.out.rectangle(100, 150, 100, 150)
    if "mouse" in Window.touching(rect):
        print("mouse")

Window.frame(main)
Window.start()


