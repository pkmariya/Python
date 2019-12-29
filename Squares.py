# creating square's using turtle

import turtle

my_turtle = turtle.Turtle()

def draw_square():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)    

draw_square()
my_turtle.forward(200)
draw_square()
