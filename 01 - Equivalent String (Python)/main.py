from list_of_tests import string1, string2, string3, string4, string5, string6, string7, string8

STRINGTEST1 = string6
STRINGTEST2 = string1


def equal_test():
    # checking if they are identical
    if len(STRINGTEST1) == len(STRINGTEST2):
        for i, charstring1 in enumerate(STRINGTEST1):
            if charstring1 != STRINGTEST2[i]:
                print("The strings aren't equal.")
                break
            print("The string are equal")
    else:
        print("The strings aren't equal.")

equal_test()

def similar_test():
    # checking what they have in common
    return 0