x = input().split(" ")
calc_logic = input().replace("x", x[0])
print(eval(calc_logic) == int(x[1]))

# input:
# 1 4
# x**3 + x**2 + x + 1
# expected output:
# True
# (1 in the formula results in 4)
# another case:
# input:
# 1 0
# x**4 - 1*x**3 + 5*x**2 - 5
# expected output:
# True