
x = 1
y = 1
z = 1
n = 3
# print only the 3 number sequence from x,y,z that does not return n when added
final_list = []
final_list.append([[value1, value2, value3] for value1 in range(0, x + 1) for value2 in range(0, y + 1) for value3 in
                   range(0, z + 1) if (value1 + value2 + value3) != n])

print(final_list[0])
