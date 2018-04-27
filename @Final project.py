######################################################################
# Author: John Martin
# Username: Martinjoh
#
# Assignment: Final project
#
#
# Purpose: Create beautiful word art to help in projects, or other activities
######################################################################
#I recieved help from Scott Hegen
#all of the 226 TA's, and vinny as well
######################################################################
from tkinter import*
from turtle import*
import turtle
class word:

    def __init__ (self, word_export, fonts, x, y):
        '''
        :param word_export: Exports word to a different file
        :param fonts: Allows user to input font
        :param x: starting x postion of the word
        :param y: starting y postion of the word
        '''
        self.user_input_word = input("Type a word:")
        self.x = x
        self.y = y
        self.fonts = fonts
        self.export = word_export





    def letter_maker(self, wordmaker, letter):
        '''
        Gives color to each letter in the word
        :param self: refrences the class
        :param wordmaker: turtle that makes the letter
        :param letter: Produces each letter individually.
        :return: None
        '''
        user_input_color = input("Choose a color for your text:") #allows user to input color
        wordmaker.color(user_input_color) #makes turtle users input color
        wordmaker.write(letter, move=False, align="left", font=(self.fonts,90, "normal")) #draws the letter with the font chosen by the user



    def word_draw(self, wordmaker):
        '''
        :param wordmaker: Turtle
        :return: None
        '''
        # self.letter_maker(wordmaker,self.user_input_word)
        for i in self.user_input_word:
            self.letter_maker(wordmaker,i) # changes the color of each letter depending on the colors the user chooses
            self.move(wordmaker) # allows word maker to create space between each letter in the word

    def move (self, wordmaker):
        '''

        :param wordmaker:
        :return: none
        '''
        wordmaker.penup()
        wordmaker.forward(110) # ammount of space between each letter in the word
        wordmaker.pendown()


    def word_export(self, expwrd):
        '''
        :param expwrd:
        :return: none
        '''
        user_file_name = (input("What is your files name?"))+ ".eps"
        readfile = open(user_file_name,"wb")
        readfile.write(expwrd)
        readfile.close()

def main():
    '''
    prints word
    :return: none
    '''
    wn = turtle.Screen()
    user_input_bcolor = input ("Choose a back ground color:") # allows user to choose backgroud color
    wn.bgcolor(user_input_bcolor)
    wordmaker= turtle.Turtle()
    wordmaker.hideturtle()
    word_information = word(fonts=input("Which font would you like to use? [vineta BT/Times New Roman/Castellar/Broadway]"), word_export=(input("What is your files name?"))+ ".eps", x=-500, y=0)
    # above code allows the user to input the fone, and give a name to the export file
    wordmaker.penup()
    wordmaker.goto(word_information.x,word_information.y)
    wordmaker.pendown()
    word_information.word_draw(wordmaker)
    wn.getcanvas().postscript(file=word_information.user_input_word) # turns pictue into postscript before it is exported
    print("Screen print the image, and open it in word or paint")
    wn.exitonclick()

main()

