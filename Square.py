import turtle
import time

square = turtle.Screen()
square.bgcolor("light blue")
square.title("Hamburger")
square_pen = turtle.Turtle()

for i in range(4):
    square_pen.forward(100)
    time.sleep(1)
    square_pen.right(90)

turtle.done()