import textwrap


def input_entry_test():
    return 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
# Expected Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


def wrap(string, max_width):
    possible_words = ''
    original_max_width = max_width
    for i, value in enumerate(string):
        possible_words += value
        if i == max_width -1:
            possible_words += "\n"
            max_width += original_max_width
    return possible_words

if __name__ == '__main__':
    string, max_width = input_entry_test()
    result = wrap(string, max_width)
    print(result)