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
snake = [[int(width / 2), int(height / 2)], [int(width / 2) - 1, int(height / 2)]] #each sub array represents the position of a segment of the snake

food_x = int(random.random() * width)
food_y = int(random.random() * height)

moving = "right"
# Can't use OOP
# lists = okay
# 2d lists = okay


def main():
    global scale, height, width, food_x, food_y, moving, snake

    Window.out.background("white")

    if Window.key.pressed("w"):
        moving = "up"

    if Window.key.pressed("s"):
        moving = "down"

    if Window.key.pressed("d"):
        moving = "right"

    if Window.key.pressed("a"):
        moving = "left"


    Window.out.color("black")
    topBorder = Window.out.rectangle(window_width/2, 2.5, window_width, 5)
    botBorder = Window.out.rectangle(window_width/2, window_height - 2.5, window_width, 5)

    snake_box = []

    for i in range(0, len(snake)):
        snake_box.append(Window.out.rectangle(snake[i][0] * scale, snake[i][1] * scale, scale, scale))

    Window.out.color("red")
    food = Window.out.rectangle(food_x * scale, food_y * scale, scale, scale)

    last_segment_x = snake[len(snake) - 1][0]
    last_segment_y = snake[len(snake) - 1][1]
    # give the previous position of the frontal segmanet to the next segment
    for row in range(1, len(snake)):
        snake[len(snake) - row][0] = snake[len(snake) - row - 1][0]
        snake[len(snake) - row][1] = snake[len(snake) - row - 1][1]

    if snake_box[0] in Window.touching(food):
        food_x = int(random.random() * width)
        food_y = int(random.random() * height)
        snake.append([last_segment_x, last_segment_y])

    # move the head
    if moving == "up":
        snake[0][1] -= 1
    if moving == "down":
        snake[0][1] += 1
    if moving == "left":
        snake[0][0] -= 1
    if moving == "right":
        snake[0][0] += 1



Window.frame(main, 100)
Window.start()
