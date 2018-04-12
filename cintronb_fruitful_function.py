######################################################################
# Author: Berucha Cintron
# Username: cintronb
#
# Assignment: T06: Funky Functions
# Purpose:  Some functions to play around with and understand return values
#           This function sings you the willaby wallaby children's song
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

def even_or_odd (num):
    """
    Is the given number even?
    :return: True or False
    """
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    """
    Determines whether the number that the user inputs is an even number
    :return: None
    """

    a = int(input("Enter any number. Is your number even?\n"))

    x = even_or_odd(a)

    print(x)

# main()
