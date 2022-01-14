import turtle
import random

def draw(n):
    if n <= 100 :
        return 0
    else:
        t.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        # t.color('')
        # t.begin_fill()
        t.forward(n)
        t.left(140)
        draw(n-2)



window = turtle.Screen()
t = turtle.Turtle()
turtle.colormode(255)
t.pensize(3)
t.speed(100)
draw(600)
window.exitonclick()
