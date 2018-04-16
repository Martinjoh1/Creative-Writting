######################################################################
# Author: John Martin
# Username: Martinjoh
#
# Assignment: A2: Loopy Turtles
#
# Purpose: Create beautiful word art to help in projects, or other activities
######################################################################
import turtle

class word:

    def __init__ (self,p=(0,0),):
            self.user_input_word=input("Type a word:")
            self.p = (0,0)




    def letter_maker(self,wordmaker,letter):
        '''
        :param self:
        :param user_input_word:
        :param user_input_color:
        :return:
        '''
        user_input_color = input("Choose a color for your text:")
        wordmaker.color(user_input_color)
        wordmaker.write(letter, move=False, align="left", font=("Arial", 75, "normal"))

    def word_draw(self,wordmaker):
        '''

        :return:
        '''
        for i in self.user_input_word:
            self.letter_maker(wordmaker,i)
            self.move(wordmaker)

    def move (self,wordmaker):
         wordmaker.penup()
         wordmaker.forward(20)
         wordmaker.pendown()




def word_export():
    pass

def main():
    """
    The main function which draws 10 shapes
    :return: None
    """
    wn = turtle.Screen()
    wordmaker= turtle.Turtle()
    wordmaker.penup()
    wordmaker.backward(200)
    wordmaker.pendown()
    word_information= word()
    word_information.word_draw(wordmaker)




main()
