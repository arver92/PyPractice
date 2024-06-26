import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

def get_random_color():
    # Returns a tuple representing an RGB color, where each color component (Red, Green, Blue) 
    # is a random integer between 0 and 255, inclusive.
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

for number_sides in range(3,11):
    turn_angle = 360/number_sides
    edge_length = 50
    tim.color(get_random_color())
    for _ in range(number_sides):
        tim.forward(edge_length)
        tim.right(turn_angle)

screen = t.Screen()
screen.exitonclick()