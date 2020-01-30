from apcs import *
import random

map = []

scale = 20
size = [10,24]
Window.size(size[0]*scale, size[1]*scale)
for i in range(size[1]):
    map.append(["grey"]*size[0])
ch = 0
cv = 0

def main():
    global map, ch, cv

    Window.out.background("black")
    s = scale/2

    def block(x,y, color, border="black"):
        Window.out.color(border)
        Window.out.square(x,y,scale)
        Window.out.color(color)
        Window.out.square(x,y,scale-4)
    
    def lell(x, y):
        lcolor = "orange"
        map[y][x] = lcolor
        map[y+1][x] = lcolor
        map[y+1][x-1] = lcolor
        map[y-1][x] = lcolor

    def rell(h, v):
        lcolor = "orange"
        map[v][h] = lcolor
        map[v-1][h] = lcolor
        map[v][h-1] = lcolor
        map[v][h-2] = lcolor
 

    def ooo(x, y):
        lcolor = "yellow"
        map[v][h] = lcolor
        map[v-1][h] = lcolor
        map[v][h-1] = lcolor
        map[v][h-2] = lcolor

    #cpiece = random.choice([rell, lell, ooo, line, zzz, ttt])

    rowc = 0
    for line in map:
        colc = 0
        for color in line:
            block(colc*scale+s, rowc*scale+s, color)
            colc += 1
        rowc += 1

    lell(5,3)

Window.frame(main)
Window.start()
    
