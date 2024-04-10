import turtle as t
import random

t.colormode(255)
stpes = 30
width = 10
tim = t.Turtle()
directions = ["right", "left"]

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_random_walk():
    tim.pensize(width)
    for _ in range(100):
        tim.forward(stpes)
        tim.color(get_random_color())
        if(random.choice(directions)=="right"):
            tim.right(90)
        else:
            tim.left(90)


draw_random_walk()
