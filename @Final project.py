######################################################################
# Author: John Martin
# Username: Martinjoh
#
# Assignment: A2: Loopy Turtles
#
# Purpose: Create beautiful word art to help in projects, or other activities
######################################################################
import turtle
import tkinter as TK
class word:

    def __init__ (self,p=(0,0),):
            self.user_input_word=input("Type a word:")
            self.p = (0,0)




    def letter_maker(self,wordmaker,letter):
        '''
        :param wordmaker:
        :param letter:
        :return:
        '''


        user_input_color = input("Choose a color for your text:")
        wordmaker.color(user_input_color)

        fonts = input("Which font would you like to use? [vineta BT/Times New Roman/Castellar/Broadway]")
        fonts_lists = ["vineta BT","Times New Roman","Castellar","Broadway"]

        while fonts in fonts_lists:
            if fonts == "vineta BT":
                wordmaker.write(letter, move=False, align="left", font=("vineta BT", 75, "normal"))
            elif fonts == "Times New Roman":
                wordmaker.write(letter, move=False, align="left", font=("Times New Roman", 75, "normal"))
            elif fonts == "Castellar":
                wordmaker.write(letter, move=False, align="left", font=("Castellar", 75, "normal"))
            elif fonts == "Broadway":
                wordmaker.write(letter, move=False, align="left", font=("Broadway", 75, "normal"))



    def word_draw(self,wordmaker):
        '''

        :return:
        '''
        for i in self.user_input_word:
            self.letter_maker(wordmaker,i)
            self.move(wordmaker)

    def move (self,wordmaker):
         wordmaker.penup()
         wordmaker.forward(40)
         wordmaker.pendown()




def word_export(expwrd):
    # tt = turtle.Turtle
    # ts = turtle.Screen()
    user_file_name = (input("What is your files name?"))+ ".eps"
    readfile = open(user_file_name,"w")
    readfile.write(expwrd)
    # tt.getscreen(ts)
    # ts.getcanvas().postscript(file= user_file_name)
    readfile.close()

def main():
    """
    The main function which draws 10 shapes
    :return: None
    """
    wn = turtle.Screen()
    user_input_bcolor = input ("Choose a back ground color:")
    wn.bgcolor(user_input_bcolor)
    wordmaker= turtle.Turtle()
    # wordmaker.hideturtle()
    # wordmaker.penup()
    # wordmaker.backward(200)
    # wordmaker.pendown()
    word_information= word()
    word_information.word_draw(wordmaker)
    word_export(word_information.user_input_word)
    wn.getcanvas().postscript(file=word_information.user_input_word)
    wn.exitonclick()




main()
