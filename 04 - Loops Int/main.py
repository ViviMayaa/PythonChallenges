
def input():
    # 5 expected : 0
    # 1
    # 4
    # 9
    # 16
    return 5

# case 1 info 1
# print not negative number before the given n while with power of 2, not including n
if __name__ == '__main__':
    n = int(input())
    number = 0
    if n >= 0:
        while number != n:
            print(number * number)
            number += 1

# case 2 info 2
# print given numbers put together including n
if __name__ == '__main__':
    n = int(input())
    number = 0
    total = ''
    while number < n:
        number += 1
        total += str(number)
    print(total)