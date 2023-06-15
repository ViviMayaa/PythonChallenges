starting_value = [0, 1]
value_given = int(input())

while value_given:
    starting_value.append(starting_value[-1] + starting_value[-2])
    value_given -= 1
print(starting_value)
max_value = 0
new_formatted_list = []
# inverting numbers
while len(starting_value):
    max_value = max(starting_value)
    new_formatted_list.append(max_value)
    starting_value.remove(max_value)
print(new_formatted_list)