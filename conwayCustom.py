import random
from apcs import *

map = []

size = [100,100]
scale = 5
Window.size(size[0]*scale, size[1]*scale)
#Window.size(500,500)

for i in range(size[0]):
    crow = []
    for n in range(size[1]):
        crow.append(False)
        #bool(random.getrandbits(1))
    map.append(crow)

def main():

    bgID = Window.out.background("white")
    mapID = []

    if Window.mouse.clicked():
        x,y = int(Window.mouse.getX()/scale), int(Window.mouse.getY()/scale)
        r = 5
        map[y][x] = not(map[y][x])
        """
        for l in range(-5,5):
            for i in range(-5,5):
                ny = y+l
                nx = x+i
                print(nx,ny)
                if ny >= 0 and ny < size[1] and nx >= 0 and nx < size[0]:
                    #if Window.key.pressed("space"):
                    #map[ny][nx] = True
                    #else:
                    map[ny][nx] = False
        """

    rc = 0
    for r in map:
        ic = 0
        crow = []
        for i in r:

            count = 0
            if not rc == 0:
                if not ic == 0:
                    if map[rc - 1][ic - 1]:
                        count += 1
                if not ic == size[0] - 1:
                    if map[rc - 1][ic + 1]:
                        count += 1
                if map[rc - 1][ic]:
                    count += 1
            if not rc == size[1] - 1:
                if not ic == 0:
                    if map[rc + 1][ic - 1]:
                        count += 1
                if not ic == size[0] - 1:
                    if map[rc + 1][ic + 1]:
                        count += 1
                if map[rc + 1][ic]:
                    count += 1
            if not ic == 0:
                if map[rc][ic - 1]:
                    count += 1
            if not ic == size[0] - 1:
                if map[rc][ic + 1]:
                    count += 1
            if Window.key.pressed("space"):
                if map[rc][ic]:
                    if count < 2:
                        map[rc][ic] = False
                    if count == 2 or count == 3:
                        map[rc][ic] = True
                    if count > 3:
                        map[rc][ic] = False
                else:
                    if count == 3:
                        map[rc][ic] = True

            if i:
                Window.out.color("black")
            else:
                Window.out.color("white")
            crow.append(Window.out.square(ic*scale+(scale/2), rc*scale+(scale/2), scale))
            #crow.append(Window.out.circle(ic * scale + (scale/2), rc * scale + (scale/2), scale)
            ic += 1

        mapID.append(crow)
        rc += 1

Window.frame(main)
Window.start()
