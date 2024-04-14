import colorgram
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
screen = t.Screen()

def get_colors_from_image():
    colors = []
    rgb_colors = colorgram.extract('image.jpg', 20)
    for color in rgb_colors:
        colors.append(color.rgb)
    return colors

def draw_painting():
    tim.hideturtle()
    tim.penup()
    screen.setup(800,800)
    tim.speed("fastest")
    start_x_position = -350
    start_y_position = -350
    end_x_position = 350
    end_y_position = 350
    dot_margin = 50
    
    colors = get_colors_from_image()
    for x_position in range(start_x_position, end_x_position, dot_margin):
        for y_position in range(start_y_position, end_y_position, dot_margin):
            tim.setposition(y_position,x_position)
            tim.dot(20,random.choice(colors))  

draw_painting()

screen.exitonclick()