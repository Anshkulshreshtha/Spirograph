from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
ak = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    combination = (r, g, b)
    return combination


ak.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        ak.color(random_color())
        ak.circle(100)
        ak.setheading(ak.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()