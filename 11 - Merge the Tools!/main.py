def merge_the_tools(string, k):
    test_array = []
    k_test = k
    for i,value in enumerate(string):
        if i< k_test :
            test_array.append(value)
        if i == k_test - 1:
            print("".join(set(test_array)))
            test_array = []
            k_test += k

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    # expected output:
    # AB
    # CA
    # AD
    merge_the_tools(string, k)