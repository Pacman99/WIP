from apcs import *

x, y, dy = 50, 20, 0

# One frame of the animation
def main():
    global x, y, dy

    # Draw the
    Window.out.background("white")
    Window.out.color("red")
    Window.out.circle(x, y, 20)

    # Move the ball.
    x = x + 3
    y = y + dy
    dy = dy + 1

    # Bounce the ball if it hits the ground.
    if y > 480:
        y = 480;
        dy = dy * -9 / 10;

print("helllo")
Window.size(500, 500)
Window.frame(main)
Window.start()
