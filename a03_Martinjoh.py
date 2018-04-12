#################################################################################
#Author: John Martin
#Username: Martinjoh
#
#Assignment: A03homework
#Purpose: To demonstrate my ability using the turtle moduels to create things
#################################################################################

import turtle


def make_skyscraper():
   '''
The base of my skyscrapper object:
   '''
turta = turtle.Turtle()

turta.shape("arrow")
turta.color("purple")
turta.penup()
turta.speed(0)
turta.pensize(10)
turta.right(90)
turta.forward(200)
turta.left(-90)
turta.forward(25)
turta.right(90)
turta.begin_fill()

for i in range (2):
    turta.pendown()
    turta.forward(390)
    turta.right(90)
    turta.forward(290)
    turta.right(90)
turta.end_fill()

def make_window1():
    '''This makes my 1st window '''
turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("Orange")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
for i in range (4):
    turtb.pendown()
    turtb.forward(50)
    turtb.right(-90)
    turtb.forward(50)
    turtb.right(-90)

def make_window2():
    '''This makes my 2nd window '''
turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("orange")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
turtb.right(-90)
turtb.forward(100)
for i in range (4):
    turtb.pendown()
    turtb.forward(50)
    turtb.right(90)
    turtb.forward(50)
    turtb.right(90)

def make_window3():
    '''This makes my 3rd window '''
turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("orange")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
turtb.right(-90)
turtb.forward(100)
turtb.forward(100)
for i in range (4):
    turtb.pendown()
    turtb.forward(50)
    turtb.right(90)
    turtb.forward(50)
    turtb.right(90)

def make_window4():
    '''This makes my 4th window '''
turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("orange")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
turtb.right(-90)
turtb.forward(100)
turtb.forward(100)
turtb.forward(50)
turtb.left(-90)
turtb.forward(100)

for i in range(4):
    turtb.pendown()
    turtb.forward(50)
    turtb.right(90)
    turtb.forward(50)
    turtb.right(90)

def make_window5():
    '''This makes my 5th window '''

turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("orange")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
turtb.right(-90)
turtb.forward(100)
turtb.forward(100)
turtb.forward(50)
turtb.left(-90)
turtb.forward(100)
turtb.left(-90)
turtb.forward(100)

for i in range(4):
    turtb.pendown()
    turtb.forward(50)
    turtb.right(-90)
    turtb.forward(50)
    turtb.right(-90)

def make_window6():
    '''This makes my 6th window '''

turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("Orange")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
turtb.right(-90)
turtb.forward(100)
turtb.forward(100)
turtb.forward(50)
turtb.left(-90)
turtb.forward(100)
turtb.left(-90)
turtb.forward(100)
turtb.forward(100)

for i in range(4):
    turtb.pendown()
    turtb.forward(50)
    turtb.right(-90)
    turtb.forward(50)
    turtb.right(-90)

def make_door():
    '''This makes my dooor to my hotel '''

turtb = turtle.Turtle()

turtb.shape("arrow")
turtb.color("red")
turtb.penup()
turtb.speed(0)
turtb.pensize(10)
turtb.right(90)
turtb.forward(200)
turtb.left(-90)
turtb.forward(25)
turtb.right(90)
turtb.forward(350)
turtb.right(90)
turtb.forward(20)
turtb.right(90)
turtb.right(-90)
turtb.forward(100)
turtb.forward(100)
turtb.forward(50)
turtb.left(-90)
turtb.forward(100)
turtb.left(-90)
turtb.forward(100)
turtb.forward(100)
turtb.left(90)
turtb.fd(100)
turtb.right(-90)
turtb.fd(50)

for i in range(2):
    turtb.pendown()
    turtb.forward(100)
    turtb.right(90)
    turtb.forward(150)
    turtb.right(90)

def make_words(shape, txt):
    """ Writes name of the buliding I've Made
    """
    shape.color("pink")
    shape.setpos(70,200)
    shape.write(txt,move=False,align='center',font=("Arial",30,("bold","normal")))

def main():
    wn =turtle.Screen()
    wn.bgcolor("black")
    make_skyscraper()
    make_window1()
    make_window2()
    make_window3()
    make_window4()
    make_window5()
    make_window6()
    make_words(turtb,"Hotel Hard work")



    wn.exitonclick()
main()
