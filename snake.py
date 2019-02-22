from apcs import *
import random

window_height = 500
window_width = 750
Window.size(window_width,window_height)

# To group tiny pixels and make rows and columns
scale = 25 # 20 columns x 30 rows
width = int(window_width / scale) #20 columns
height = int(window_height / scale) # 30 rows

# Starting position
snake_x = int(width / 2)
snake_y = int(height / 2)

# food_x = int(math.random() * width)
# food_y = int(math.random() * height)

moving = "right"
# Can't use OOP
# lists = okay
# 2d lists = okay


def main():
    global scale, height, width, snake_x, snake_y, moving

    Window.out.background("white")

    if Window.key.pressed("w"):
        moving = "up"

    if Window.key.pressed("s"):
        moving = "down"

    if Window.key.pressed("d"):
        moving = "right"

    if Window.key.pressed("a"):
        moving = "left"


    if moving == "up":
        snake_y -= 1
    if moving == "down":
        snake_y += 1
    if moving == "left":
        snake_x -= 1
    if moving == "right":
        snake_x += 1


    Window.out.color("black")
    topBorder = Window.out.rectangle(window_width/2, 2.5, window_width, 5)
    botBorder = Window.out.rectangle(window_width/2, window_height - 2.5, window_width, 5)

    # snake = Window.out.rectangle(snake_x * scale, snake_y * scale, scale, scale)
    # food = Window.out.rectangle(food_x * scale, food_y * scale, scale, scale)

Window.frame(main, 100)
Window.start()
