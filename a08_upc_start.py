######################################################################
# Author: John Martin        TODO: Change this to your names
# Username: MartinJoh            TODO: Change this to your usernames
#
# Assignment: A08: UPC Bar Codes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle

#guard=[]
#upc=[]
# draw(    ,hieight )
#if color == 0
    # t.color ("black")
    #t.begin_fill
    #draw rectangle
    #t.end_fill()

def is_valid_input(barcode):
    '''
    :param barcode: 
    :return: 
    '''

    if int(len(barcode)) == 12: #checks if line is right length, and has the propper amount of numbers
        return True
    else:
        return False

def convert_to_list (input_code):
    '''

    :param input_code: 
    :return: Turns users input into a list
    '''

    converted_input= list(str(input_code)) #Turns user input into list that is mutuable
    #print(converted_input)
    return converted_input

def is_valid_modulo(upc_list):
    '''
    Couter (any variable name ) before for loop, set counter to zero
    Odd (0) and even (1) <---- (what to start with)
    loop through add i to different variable that starts out as zeor
    add to that other variable
    add pluse two to the counter in the for loop

    :param upc_list:
    :return: Upc_list with modulo check number appended to the end
    '''
    even_sum = 0
    odd_sum = 0
    #modulo=upc_list[0:11]
    for num in upc_list:
        if int(num) % 2 == 0: #takes the remainder of num divided by 2
            even_sum += int(num)
            #print("even_sum=" + str(even_sum))
        else:
            odd_sum += int(num)
            #print("odd sum = " + str(odd_sum))
    total_sum= even_sum + 3*odd_sum #adds even sum to the odd sum multiplied by 3
    #print("total sum = " + str(total_sum))
    equation_number = int(total_sum) % 10
    #print("equation num = " + str(equation_number))
    if equation_number > 0:
        check_number = 10 - equation_number
        print(str(check_number))
        upc_list.append(check_number)
    else:
        return total_sum
    return upc_list

def convert_binary(upc_barcode_list):
    """
    
    :param upc_barcode_list: 
    :return: 
    """
    translatorleft = {"0":"0001101", #Makes a class for each of the numbers binary equals
                            "1":"0011001",
                            "2":"0010011",
                            "3":"0111101",
                            "4":"0100011",
                            "5":"0110001",
                            "6":"0101111",
                            "7":"0111011",
                            "8":"0110111",
                            "9":"0001011"}
    translatorright = {"0":"1110010",
                            "1":"1100110",
                            "2":"1101100",
                            "3":"1000010",
                            "4":"1011100",
                            "5":"1001110",
                            "6":"1010000",
                            "7":"1000100",
                            "8":"1001000",
                            "9":"1110100"}
    guardbar= "101"
    centerbar= "01010"
    binaryleft = ""
    binaryright= ""
    for x in upc_barcode_list[0:7]:
        if x in translatorleft.keys():
            binaryleft += str(translatorleft[x])
            #print(str(binaryleft))
        else:
            return "?"
    for i in upc_barcode_list[7:]:
        if i in translatorright.keys():
            binaryright += str(translatorright[i])
    print (guardbar + binaryleft + centerbar + binaryright + guardbar)
    return guardbar + binaryleft + centerbar + binaryright + guardbar #combines binary to form binary version of barcode

def binary_image(binary):
    '''

    :param binary:
    :return: none
    '''
    guard=[]
    upc=list(binary)
    binny = turtle.Turtle()
    binny.speed(0)
    binny.pensize(4)
    binny.shape("arrow")
    binny.penup()
    binny.setpos(-200,150)
    binny.pendown()
    (x,y)= binny.pos()
    for i,e in enumerate(upc):
        if e == "1":
            binny.goto(x,y-200)
        binny.goto(x,y)
        x+=4
        binny.penup()
        binny.goto(x,y)
        binny.pendown()


def make_numbers(input_code):
    '''

    :param input_code:
    :return: None
    '''
    bin = turtle.Turtle()
    bin.speed(0)
    bin.pensize(4)
    bin.shape("arrow")
    bin.penup()
    bin.right(90)
    bin.forward(100)
    bin.right(90)
    bin.forward(50)
    bin.pendown()
    bin.write(input_code,False,"center",("Arial",20,"normal"))

def main():
    wn = turtle.Screen()
    input_code = input("Enter a 12 digit code [0-9]: ")
    while not is_valid_input(input_code):
        input_code = input("Invalid number. Enter a 12 digit code [0-9]: ")
    upc_list = convert_to_list(input_code)
    upc_barcode_list = is_valid_modulo(upc_list)
    upc_binary=convert_binary(upc_barcode_list)
    binary_image(upc_binary)
    make_numbers(input_code)
    wn.exitonclick()



if __name__ == "__main__":
    main()
