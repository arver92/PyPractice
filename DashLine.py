import turtle as t

def draw_dash_line():
    tim = t.Turtle()
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


draw_dash_line()

screen = t.Screen()
screen.exitonclick()