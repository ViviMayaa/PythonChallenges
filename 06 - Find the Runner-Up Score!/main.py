def input():
    number_list = [2, 3, 6, 6, 5]
    # returns 5, second highest number
    # number_list = [57, 57, -57, 57]
    # number_list = [5, 5, 6]

    return number_list


if __name__ == '__main__':
    arr = input()
    high_score = 0
    second_high_score = 0
    high_score = max(arr)
    # for value in arr:
    #     if value >= high_score:
    #         high_score = value
    for value in arr:
        if value > second_high_score and value != high_score:
            second_high_score = value
        elif value < 0 and second_high_score == 0:
            second_high_score = value

    print(second_high_score)