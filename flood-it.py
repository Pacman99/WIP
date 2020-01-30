from apcs import *
import random
from sys import exit

size = [42,42]
scale = 15
ncolors = 8
map = []
colors = ["red", "orange", "blue", "green", "purple", "pink", "violet", "turquoise", "gold", "gray", "brown"]
colors = colors[:ncolors]
moveCount = 0
maxMoves = int(25*((size[1]+size[0])*ncolors)/((14+14)*6))
Window.size(size[0]*scale, size[1]*scale)

for l in range(size[0]):
    crow = []
    for i in range(size[1]):
        if i == 0 and l == 0:
            crow.append([True, random.choice(colors)])
        else:
            crow.append([False, random.choice(colors)])
    map.append(crow)

ccolor = map[0][0][1]

def main():
    Window.out.background("white")
    global ccolor
    global moveCount
    global maxMoves
    winCount = 0
    prevMap = map
    x, y = int(Window.mouse.getX() / scale), int(Window.mouse.getY() / scale)

    moveText = str(moveCount) + "/" + str(maxMoves)
    Window.out.color("black")
    Window.out.text(moveText, size[0] * scale + 45, 25)

    if Window.mouse.clicked():
        if y >= 0 and y < size[1] and x >= 0 and x < size[0]:
            ccolor = map[y][x][1]
        if ccolor != map[0][0][1]:
            moveCount += 1
    if Window.key.pressed("space"):
        print(map[y][x])

    rc = 0
    for row in map:
        ic = 0
        for box in row:
            if box[0]:
                winCount += 1
            if ccolor:
                if box[0]:
                    map[rc][ic][1] = ccolor
                else:
                    if box[1] == ccolor:
                        if not rc == 0:
                            if map[rc-1][ic][0]:
                                map[rc][ic][1] = ccolor
                                map[rc][ic][0] = True
                        if not rc == size[1]-1:
                            if map[rc+1][ic][0]:
                                map[rc][ic][1] = ccolor
                                map[rc][ic][0] = True
                        if not ic == 0:
                            if map[rc][ic-1][0]:
                                map[rc][ic][1] = ccolor
                                map[rc][ic][0] = True
                        if not ic == size[0]-1:
                            if map[rc][ic+1][0]:
                                map[rc][ic][1] = ccolor
                                map[rc][ic][0] = True

            Window.out.color(map[rc][ic][1])
            Window.out.square(ic*scale+(scale/2), rc*scale+(scale/2), scale)
            #Window.out.circle(ic * scale + (scale / 2), rc * scale + (scale / 2), scale/2)
            ic += 1
        rc += 1

    winNeeded = size[0] * size[1]
    if moveCount >= maxMoves and winCount < winNeeded:
        Window.out.color("black")
        Window.out.text("Game Over You Lose", size[0] * scale / 2, size[1] * scale / 2)
    if winCount  >= winNeeded and moveCount <= maxMoves:
        Window.out.color("black")
        Window.out.text("You Win", size[0]*scale/2, size[1]*scale/2)
        #print("You Win")

Window.frame(main)
Window.start()