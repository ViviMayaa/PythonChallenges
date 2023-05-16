NAMES = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
SCORES = [37.21, 37.21, 37.2, 41, 39]


if __name__ == '__main__':
    scores_list = []
    names_list = []
    second_lowest_names = []
    second_lowest_names_formatted = []
    total = 0
    for _ in range(len(SCORES)):
        name = NAMES[_]
        score = SCORES[_]
        scores_list.append(score)
        names_list.append(name)
    second_lower_number = 10000000
    lower_number = 10000000
    for number in scores_list:
        if number < lower_number:
            lower_number = number
    for number in scores_list:
        if number != lower_number and number < second_lower_number:
            second_lower_number = number
    for i, number in enumerate(scores_list):
        if number == second_lower_number:
            total += 1
            second_lowest_names.append(names_list[i])
    second_lowest_names_formatted.append(sorted(second_lowest_names))
    for i in range(total):
        print(second_lowest_names_formatted[0][i])
