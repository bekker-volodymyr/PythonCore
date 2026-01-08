# import math
# import random

# # r = random.randint(10, 15)
# f = math.factorial(20)

from math import factorial
from random import randint

r = randint(10, 15)
f = factorial(20)

print(f"Random number: {r}\nFactorial of 20: {f}")

import turtle

turtle.shape('turtle')
turtle.pensize(5)
turtle.color('green')

turtle.circle(100)
turtle.forward(125)
turtle.right(90)
turtle.backward(200)
turtle.left(20)
turtle.forward(40)
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.goto(35, 68)
turtle.pendown()
turtle.circle(randint(25, 100))


def square(side, color='green', fill_color=None):
    turtle.color(color)
    if(fill_color):
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)

    if(fill_color):
        turtle.end_fill()


turtle.goto(1, 1)
square(150, 'yellow', 'pink')
turtle.goto(150, 150)
square(35, 'red', 'purple')

screen = turtle.Screen()

screen.onkey(lambda: turtle.forward(15), 'w')
screen.onkey(lambda: turtle.backward(15), 's')
screen.onkey(lambda: turtle.right(5), 'd')
screen.onkey(lambda: turtle.left(5), 'a')

screen.listen()

turtle.done()