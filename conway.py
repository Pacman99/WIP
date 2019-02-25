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
            crow.append(Window.out.square(ic*10+5, rc*10+5, 10))
            ic += 1

        mapID.append(crow)
        rc += 1

    #if Window.mouse.clicked():



Window.frame(main)
Window.start()
