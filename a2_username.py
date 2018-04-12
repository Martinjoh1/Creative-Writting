######################################################################
# Author: John Martin
# Username: Martinjoh
#
######################################################################
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
john = turtle.Turtle()
john.shape("arrow")
john.color("red")

john.penup()
john.backward(100)
john.right(90)
john.pendown()
john.forward(200)
john.left(75)
john.forward(50)
john.left(40)
john.forward(50)
john.left(65)
for side in range (40):  #Loops stamps in order to make them go in one long line
    john.stamp()
    john.forward(10)

jn = turtle.Turtle()
jn.shape("circle")
jn.color("lightblue")
jn.penup()
jn.right(-90)
jn.forward(210)
jn.right(90)


for side in range(3):# Must include col, and Dep, and not make number too large for program to work
    colors = ["green", "blue", "violet"]
    for col in colors:
        for dep in range(3):
            jn.color(col)
            jn.forward(4.5)
            jn.stamp()

jm = turtle.Turtle()
jm.shape("circle")
jm.color("lightblue")
jm.penup()
jm.right(-90)
jm.forward(210)
jm.left (90)


for side in range(3):
    colors = ["yellow", "orange", "red",]
    for col in colors:
        for dep in range(3):
            jm.color(col)
            jm.forward(4.5)
            jm.stamp()







wn.exitonclick()





