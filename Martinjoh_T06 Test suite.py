######################################################################
# Author: John Martin      
# Username: Martinjoh             
#
# Assignment: T06: Funky Functions Test Suite
# Purpose:  Test suite to test the willoughby_wallaby function in t06_funky_functions.py
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys

from cintronb_fruitful_function import *


def testit(did_pass):
    """

    :param did_pass:
    :return:
    """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line (0) ok.".format(linenum)
    else:
        msg = "Test at line (0) failed.".format(linenum)
    print(msg)


def even_or_odd_test_suite():
    print("\nRunning the even_or_odd_test_suite()).")
    testit(even_or_odd(2) == True)          # test even number  
    testit(even_or_odd(4.0) == True)        # test even float
    testit(even_or_odd(19) == False)        # test odd
    testit(even_or_odd(-20) == True)        # test negative even
    testit(even_or_odd(200) == True)        # test even number larger than 100
    testit(even_or_odd(-19) == False)       # test negative odd
    testit(even_or_odd(17.0) == False)      # test floating odd
    testit(even_or_odd(1900) == True)       # test even larger than 1000
    testit(even_or_odd(194989) == False)    # test odd larger than 10000
    print("\nEnding the even_or_odd_test_suite()).")


def main():
    '''
    :return: None
    '''
   
    even_or_odd_test_suite()


if __name__ == '__main__':
    main()
