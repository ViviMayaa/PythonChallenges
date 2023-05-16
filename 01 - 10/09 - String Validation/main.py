if __name__ == '__main__':
    test_value = 'qA2'
    # expect all True
    num = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for value in test_value:
        if value.isalnum():
            num = True
        if value.isalpha():
            alpha = True
        if value.isdigit():
            digit = True
        if value.islower():
            lower = True
        if value.isupper():
            upper = True
    list_s = [num, alpha, digit, lower, upper]
    print(*list_s, sep="\n")
