from turtle import Turtle, Screen

tim = Turtle()
tim.color("black")
tim.shape("turtle")

for i in range(0,4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()