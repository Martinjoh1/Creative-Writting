######################################################################
# Author: Berucha Cintron, Bethanie Williams, John Martin
# Username: cintronb, williamsbe, martinjoh
#
# Assignment: T07: Turtle Art
#
# Purpose: Create beautiful works of art through code, namely iterations
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random


def draw_shapes(turt):
    # FIXME modify this function so that it's more general
    """
    Draws randomly colored shapes using the turtle library
    :param turt: a turtle object to draw with
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))     # gives the turtle a random color
    turt.speed(0)
    while True:
        for num in range (3,1000):
            turt.forward(360 % num)
            turt.left(360 % num)           # the angle ensures a perfect hexagon





def main():
    # FIXME modify the docstring so it's correct for your final code
    """
    The main function which draws 10 hexagons
    :return: None
    """
    t = turtle.Turtle()
    wn = turtle.Screen()
    # Draws 10 hexagons
    for num in range(10):
        t.penup()
        # Move the turtle to a random place on the screen
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()

        draw_shapes(t)

    wn.exitonclick()

main()
