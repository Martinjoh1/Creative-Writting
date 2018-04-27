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
You'll complete this part at the end of the project. In this section, add a publicly available link to a YouTube video which you will create, demonstrating how to use your program. The video is a short (less than 5 minutes) demonstration video. Your video should include:

A title screen, including the class name, your name, and the project title
You briefly discussing your project and it's motivation
A demonstration on how to use the program, much like a marketing video.
A short discussion about what you learned through the process of building the program.
DO NOT include a section where you scroll through the code. Your video should include NO code.
A credits roll
Instructions
Explain how to use your program and/or play your game.

# Errors
- Does not print exact image of turtle screen when exported only prints letters, and colors.
- Spacing between letters is not even.


# Reflection
You'll complete this part at the end of the project. Write a paragraph or two of your reactions to the final project.

# References
Throughout this project, you've likely used outside resources. Reference all ideas or code which are not your own, and describe and how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution.

A Note From Scott to You
While there seems like a lot of work around this final project, one thing to keep in mind is HAVE FUN with it! You are creating code to express your interests. Make a fun video. Break up the writing so it’s not so burdensome. We will have a live demo session on our last day of class. It'll be the most fun final exam you've ever had!

