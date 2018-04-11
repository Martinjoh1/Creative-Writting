# Feedback

I like your idea! Should be visually appealing.

Your CRC is impossible to read, because you didn't follow the instructions I provided. If they were unclear, ask for help. I will give as much feedback as I can based on what I can glean from the file.

Your class collaborations are muddled with your class attributes. I think you've got terminology wrong. 

There are a lot of typos. For example, I think you meant __init__() instead of __int__(). It matters; one overloads the initializer for the class (correct), the other overloads the int() method which converts strings to integers (wrong!). This particular typo could cost a company millions!


You should have at least one more attribute: self.word

Not sure what self.draw is. A flag for which style to draw? 

In your (supposed) init(), it says "draws the letter...", but the class is called Word. Does this class draw a word in a particular style, or a letter, each in different styles? It sounds like the former from your description, but the latter is what your CRC card is describing.

You probably don't need a method for every user input. Each method will have one line of code in it (maybe more, if you validate every input, i.e., check that a color is a valid color choice, etc. One method for user_input() would probably suffice.

Word_draw() says it's using a letter dictionary. I didn't see a letter dictionary defined in your CRC card.

Word_expert() is unclear. Is it creating an image from the turtle drawing? If so, do you know how to convert it? I don't...

In the files section, you listed 10 files. None of those files are in the repo. Additionally, you didn't include the files you're creating for your project (the word.py file for the class, plus a word_main.py that runs the code, plues the words_test.py test suite). 

I like the idea, but it needs more defined.

Grade: 6/10

