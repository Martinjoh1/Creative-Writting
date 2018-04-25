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

    def __init__ (self,fonts,p=(0,0)):
            self.user_input_word=input("Type a word:")
            self.p = (0,0)
            self.fonts= fonts




    def letter_maker(self,wordmaker, letter):
        '''
        :param wordmaker:
        :param letter:
        :return:
        '''


        user_input_color = input("Choose a color for your text:")
        wordmaker.color(user_input_color)
        wordmaker.write(letter, move=False, align="left", font=(self.fonts, 75, "normal"))


    def word_draw(self,wordmaker):
        '''

        :return:
        '''
        # self.letter_maker(wordmaker,self.user_input_word)
        for i in self.user_input_word:
            self.letter_maker(wordmaker,i)
            self.move(wordmaker)

    def move (self,wordmaker):
         wordmaker.penup()
         wordmaker.forward(70)
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
    wordmaker.hideturtle()
    wordmaker.penup()
    wordmaker.backward(200)
    wordmaker.pendown()
    fonts = input("Which font would you like to use? [vineta BT/Times New Roman/Castellar/Broadway]")
    word_information= word(fonts)
    word_information.word_draw(wordmaker)
    word_export(word_information.user_input_word)
    wn.getcanvas().postscript(file=word_information.user_input_word)
    wn.exitonclick()




main()
