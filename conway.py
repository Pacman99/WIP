import random
from apcs import *

map = []

size = [50, 50]
Window.size(size[0]*10, size[1]*10)
#Window.size(500,500)

for i in range(size[0]):
    crow = []
    for n in range(size[1]):
        crow.append(bool(random.getrandbits(1)))
    map.append(crow)

def main():

    bgID = Window.out.background("white")
    mapID = []
    rc = 0
    for r in map:
        ic = 0
        crow = []
        for i in r:


            if i:
                Window.out.color("black")
            else:
                Window.out.color("white")
            crow.append(Window.out.square(ic*10+5, rc*10+5, 10))
            ic += 1

        mapID.append(crow)
        rc += 1

    if Window.mouse.clicked():
        ic,rc = int(Window.mouse.getX()/10), int(Window.mouse.getY()/10)
        count = 0
        if map[ic - 1][rc - 1]:
            count += 1
        if map[ic][rc - 1]:
            count += 1
        if map[ic + 1][rc - 1]:
            count += 1
        if map[ic + 1][rc]:
            count += 1
        if map[ic + 1][rc + 1]:
            count += 1
        if map[ic][rc + 1]:
            count += 1
        if map[ic - 1][rc + 1]:
            count += 1
        if map[ic - 1][rc]:
            count += 1
        print(count)


Window.frame(main)
Window.start()
