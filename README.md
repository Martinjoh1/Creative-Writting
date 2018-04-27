# Motivation
I am building this program in order to make typing a more creative and fun experience.
I hope to build a progrma that allows people to type a word, and then make that word artistically using the trutle. 
There should be different colors, and letters should be filled, the users should be able to input a word, and colors, and than 
their word should be given with their specified colors. It should be fun, and interesting, and the person should want to come back for more. It is also a great help to people who cannot draw large letters creatively. 

# Purpose
Build  a progamr that makes word art a process that anyone can partake in. 

# Initial Design Plan


Class name: Word
Class Attributes:  Turtle class


Class Collaborations (other classes):
Self.draw	# gives instructions for drawing each letter
Self.Color 	# allows turtle to take in different colors when drawing the letters
Self.x		#gives starting x positon for the letters
Sel.y 		#gives starting y position for the lettes
  


Class Methods: 

Class Collaborations (other classes):
Turtle class 

__int__():
Draws the letter starting in the (x,y position which stays the same)

User_input_color ():
Takes in the users word input for color

User_input_ Word():
Takes in the users word input

letter Dictionary ():
Creates a dictionary that connects each word to a number

Word_draw():
Draws the word based on the input given by the user, and the using the letter dictionary to design the word

Word_export(): 
Sends the word to a seperate file, for the user to print it off and use it. 


# Files
T03 (This helps to use turtles artistically)
T13 (This will help me set up the class)
T14 (helps set up letter dictionary)
T10 (Helps to positon turtles)
T02 (Helps in basic uderstanding and use of turtles)
T06 (Artistic use of turtles)
T07 (Artistic use of turtles)
A03 (positioning, and use of turtles)
A02 (use of turtles)
A08 (Helps wo make the letter dictionary, which helps to make the words)


# Summary
  This program was hard to create, but it was fun as well. I spent about over 8 hours working on  the project trying to make it look right, or do what I wanted with more efficeintly. The word grew to include font and export attributes, and p attribute was replaced with an x and y. Font allows the user to choose the font, and export allows the user to title the file being export. The final result is a progrma that lets the user type in a word, and then put in colors for each letter of that word. The user is then abel to export this file in Eps., and is encouraged to screenshot the final image. 
  
  I encountered at least one challenge that was not specifically required. I had to find a way for the turtle screen to be printed as an image. In this process i dowonloaded ghostscript, and coded my program so that it turned the turtle screen into postcript, and exported it as eps., so that it could be read by ghostscript. This is something we had never done in class, and i was happey to have accomplished something new. 

# Video
https://youtu.be/c_DeqWKiVxo

# Errors
- Does not print exact image of turtle screen when exported only prints letters, and colors.
- Spacing between letters is not even.
- If word is too large it will not fit the entire screen, but if multiple words each word can be ran seperately.
- program automatically ends if there are spaces or the color and font is typed incorrectly.

# Reflection
I really love my final project, because i know how much time and effort went into it. I am also happy with how much I learned. I now know about postscript, how to use classes more accurately. How to create objects, and attributes. I can get turtles to be used interactively with classes. I am also able to make cool and interesting art like objects on the computer. I beleve the program i made is something anyone would sit down, and play with just to see what they made. I am not happy because really large words might not fit the entire screen, because I could not let users choose a font size or eles the spacing would be really bad, and I was not able to make the image screen print automatically. I feel as if there was a lot I could have done, and that I also acomplished a lot as well.

I came up with this idea, created a mediocore design, and was helped to make it more realistic and honestly better. I had not thought through every posibility, or really contemplated what was capable, but, I am glad that I did this. The class and this project has helped me to be more critical, and to really think about every option before taking action. I also have learned how to map things out more accurately in my mind. Starting off I had never done computer science before, but now I feel as if I am starting to understand. I am grasping the flow of the code more easily. This is one of the times when I have learned the most. 

# References
- https://stackoverflow.com/questions/4071633/python-turtle-module-saving-an-image (I used this to help me export the turtle image as enhanced post script)
-T14, T13, T02, and T10 (helped me to use classes more effeicently, and to help with my understanding of how exactly to use turtles in the program itself.) 
_ All CSC 226 TA's, Berucha, and Patrick (They all hleped me to better understand and impliment classes, and made the project more enjoyable :) )

