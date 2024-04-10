import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")

def get_random_color():
    # Returns a tuple representing an RGB color, where each color component (Red, Green, Blue) 
    # is a random integer between 0 and 255, inclusive.
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

for turn_angle in range(0,361,10):
    tim.circle(100)
    tim.color(get_random_color())
    tim.setheading(turn_angle)
    
screen = t.Screen()
screen.exitonclick()