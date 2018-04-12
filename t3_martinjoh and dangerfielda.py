######################################################################
# Author: Annette and John             TODO: Change this to your name, if modifying
# Username: dangerfielda and martinjoh                     TODO: Change this to your username, if modifying
#
# Assignment: T3: Boustrophedon Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes and using images for shapes
######################################################################

import turtle

def draw_square(turta, size):
    for side in range(2):
        turta.forward(500)
        turta.right(90)
        turta.forward(500)
        turta.right(90)


'''Draws a square with turta'''


def turtle_fill(turtb):
    for i in range(11):
        turtb.forward(462)
        turtb.left(90)
        turtb.forward(20)
        turtb.left(90)
        turtb.forward(462)
        turtb.right(90)
        turtb.forward(20)
        turtb.right(90)


'''Fills in the square with turtb'''


def turt_fill2(turtb):
    for i in range (1):
        turtb.forward(462)
        turtb.left(90)
        turtb.forward(20)
        turtb.left(90)
        turtb.forward(462)

def main():
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("We're boustrophedon with this square!")

    turta = turtle.Turtle()
    turta.shape("arrow")
    turta.color("pink")
    turta.pensize(20)

    turta.penup()
    turta.left(135)                 # moves turta to the top left of the screen to center the square
    turta.forward(295)
    turta.right(135)
    turta.pendown()

    draw_square(turta, 500)         # draws the square

    turtb = turtle.Turtle()
    turtb.shape("arrow")
    turtb.color("purple")
    turtb.pensize(20)

    turtb.penup()
    turtb.right(125)                # moves turtb to the lower right corner of the square to begin fill
    turtb.forward(330)
    turtb.left(125)
    turtb.pendown()
    turtb.speed(0)

    turtle_fill(turtb)
    turt_fill2(turtb)

    wn.exitonclick()
main()
