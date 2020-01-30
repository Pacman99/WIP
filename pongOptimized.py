from apcs import *
import random

wheight = 500
wwidth = 750
wcent = [wheight/2, wwidth/2]
Window.size(wwidth,wheight)

#x = 0
#     xCoord, yCoord, score
p1 = [wwidth-20, wheight/2, 0]
p2 = [20, wheight/2, 0]
#      xCoord,    yCoord       angle
pongSpeed = 3
pong = [wwidth/2, wheight/2, random.randint(1, 360)]

if 0:
    print(pong[2], pong[3])

def main():
    #global x
    global p1, p2, pong

    Window.out.background("white")
    Window.out.color("black")

    x = Window.mouse.getX()
    y = Window.mouse.getY()

    speed = 10
    pongRadius = 14
    rectHeight = 85
    rectWidth = 20

    if Window.key.pressed("i"):
        p1[1] -= speed

    if Window.key.pressed("k"):
        p1[1] += speed

    if Window.key.pressed("w"):
        p2[1] -= speed

    if Window.key.pressed("s"):
        p2[1] += speed

    if p1[1] < rectHeight/2:
        p1[1] = rectHeight/2

    if p1[1] > wheight - (rectHeight/2):
        p1[1] = wheight - (rectHeight/2)

    if p2[1] < rectHeight / 2:
        p2[1] = rectHeight / 2

    if p2[1] > wheight - (rectHeight / 2):
        p2[1] = wheight - (rectHeight / 2)

    if pong[2] > 1 and pong[2] <= 90:
        refAngle = pong[2]
    elif pong[2] > 90 and pong[2] <= 180:
        refAngle = 180 - pong[2]
    elif pong[2] > 180 and pong[2] <= 270:
        refAngle = pong[2] -180
    elif pong[2] > 270 and pong[2] <= 360:
        refAngle = 360 - pong[2]

    topBorder = Window.out.rectangle(wwidth/2, 2.5, wwidth, 5)
    botBorder = Window.out.rectangle(wwidth/2, wheight - 2.5, wwidth, 5)

    p1Goal = Window.out.rectangle(2.5, wheight/2, 5, wheight)
    p2Goal = Window.out.rectangle(wwidth-2.5, wheight / 2, 5, wheight)

    p1ID = Window.out.rectangle(p1[0], p1[1], rectWidth, rectHeight)
    p2ID = Window.out.rectangle(p2[0], p2[1], rectWidth, rectHeight)

    pong[0] += pong[2]
    pong[1] += pong[3]
    pongID = Window.out.circle(pong[0], pong[1], pongRadius)

    if pongID in Window.touching(topBorder):
        pong[3] *= -1

    if pongID in Window.touching(botBorder):
        pong[3] *= -1

    if pongID in Window.touching(p1Goal):
        p1[2] += 1
        pong = [wwidth / 2, wheight / 2, random.choice([-3, 3]), random.uniform(-6, 6)]
        pong[2] *= pongSpeed
        pong[3] *= pongSpeed

    if pongID in Window.touching(p2Goal):
        p2[2] += 1
        pong = [wwidth / 2, wheight / 2, random.choice([-3, 3]), random.uniform(-6, 6)]
        pong[2] *= pongSpeed
        pong[3] *= pongSpeed

    if pongID in Window.touching(p1ID):
        pong[2] *= -1
        pong[3] *= -1
        pong[3] += random.uniform(-1, 1)
        pong[2] += random.uniform(-.5,.5)

    if pongID in Window.touching(p2ID):
        pong[2] *= -1
        pong[3] *= -1
        pong[3] += random.uniform(-3, 3)
        pong[2] += random.uniform(-3, 3)

    Window.out.color("grey")
    Window.out.line(wwidth/2, 5, wwidth/2, wheight - 5)
    Window.out.text(str(p1[2]), wwidth/2 + 20, 25)
    Window.out.text(str(p2[2]), wwidth/2 - 20, 25)

Window.frame(main)
Window.start()
