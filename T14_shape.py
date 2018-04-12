######################################################################
# Author: Berucha Cintron, John Martin
# Username: cintronb, martinjoh
#
# Assignment: T14: Crazy Shapes
#
# Purpose:  Demonstrate the collaboration between classes, such as using a point to create a rectangle
######################################################################
# Acknowledgements:
#
# Original code created by Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


import turtle
import random
from t14_point import Point

class Shape:
    '''

    '''
    def __init__ (self,posn=Point(0,0)):
        """

        :rtype: object
        """
        self.start_point = posn
        self.num_sides = int(input("Enter the number of sides you want your shape to have:"))
        self.side_length = int(input("Enter the length you want your sides to be:"))
        self.t = turtle.Turtle()

    def draw_shape(self):  # black is the default color
        """
        Instantiates a Turtle object and draws a shape on the Screen

        :return: None
        """
        self.t.penup()
        self.t.goto(self.start_point.x, self.start_point.y)
        self.t.color((random.random(), random.random(),random.random()))
        self.t.pendown()

        for num in range(self.num_sides):
            self.t.left(360/self.num_sides)
            self.t.forward(self.side_length)


def main():
    """
    The main function which draws 10 shapes
    :return: None
    """
    wn = turtle.Screen()
    # Draws 10 shapes
    for num in range(10):
        # Move the turtle to a random place on the screen
        t = Shape()
        t.draw_shape()

    wn.exitonclick()

main()


