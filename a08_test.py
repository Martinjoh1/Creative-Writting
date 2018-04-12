from a08_upc_start import *
import sys

def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def a7_test_suite():
    testit(is_valid_input("1") == False)
    testit(is_valid_input("123456789012")== True)
    testit(is_valid_input("123B56789012")== True)
    testit(is_valid_input("123456789019")== True)
    testit(is_valid_input("12345678901 ")== True)

def convert_test_suite():
    '''

    :return: List of binary of number
    '''
    testit(convert_to_list(101010101010)== ["1","0","1","0","1","0","1","0","1","0","1","0"])
    testit(convert_to_list(999999999999)== ["9","9","9","9","9","9","9","9","9","9","9","9"])
    testit(convert_to_list(123456789012)== ["1","2","3","4","5","6","7","8","9","0","1","2"])

def is_valid_modulo_test_suite():
    '''

    :return: List with appeneded check number
    '''
    testit(is_valid_modulo(["9","9","9","9","9","9","9","9","9","9","9","9"])== ["9","9","9","9","9","9","9","9","9","9","9","9","6"])
    testit(is_valid_modulo(["1","1","1","1","1","1","1","1","1","1","1","1"])== ["1","1","1","1","1","1","1","1","1","1","1","1","4"])
    testit(is_valid_modulo(["1","2","3","4","5","6","7","8","9","0","1","2"])== "Error")
    testit(is_valid_modulo(["1","0","1","0","1","0","1","0","1","0","1","0"])== ["1","0","1","0","1","0","1","0","1","0","1","0","2"])

def convert_binary():
    '''

    :return: Binary for the barcode
    '''
    testit(convert_binary(["1","0","9","2","8","7","6","3","5","4","2","5"]) == "10100110010001101000101100100110110111011101101011110101010000101001110101110011011001001110101")
    testit(convert_binary(["1","0","1","0","1","0","1","0","1","0","1","0"]) == "10100110010001101001100100011010011001000110100110010101011100101100110111001011001101110010101")
    testit(convert_binary(["9","9","9","9","9","9","9","9","9","9","9","9"]) == "10100010110001011000101100010110001011000101100010110101011101001110100111010011101001110100101")
def main():
    a7_test_suite()
    is_valid_modulo_test_suite()
    convert_test_suite()
    convert_binary()

if __name__ == "__main__":
    main()
