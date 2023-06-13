def count_substring(string, sub_string):
    test_substring = ""
    count = 0
    string += " "
    for value in string:
        if len(test_substring) == len(sub_string):
            if test_substring == sub_string:
                count += 1
            test_substring = test_substring.replace(test_substring[0:1], "", 1)
        test_substring += value

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

    # input:
    # ABCDCDC
    # CDC
    # expected output:
    # 2
