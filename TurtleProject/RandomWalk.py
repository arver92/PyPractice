import turtle as t
import random

t.colormode(255)
stpes = 30
width = 10
tim = t.Turtle()
directions = [0,90,180,270]

def set_random_direction():
    tim.setheading(random.choice(directions))

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_random_walk():
    tim.pensize(width)
    for _ in range(100):
        tim.forward(stpes)
        tim.color(get_random_color())
        set_random_direction()


draw_random_walk()
