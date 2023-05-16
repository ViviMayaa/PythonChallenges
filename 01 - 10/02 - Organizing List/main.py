sellers = '2, 3, 6, 8, 3'
x_seller = '8'
amount_of_sells = 10
value = []
# moving the queue up
for item in sellers:
    if item == "'" or item == " " or item == ",":
        pass
    else:
        value.append(item)
for _ in range(amount_of_sells):
    first_value = value[0]
    value.pop(0)
    value.append(first_value)
    print(value)

position = 0
# finding how long it takes for an ID to get in first place
for item in value:
    position += 1
    if item == x_seller:
        break

print(f"The seller {x_seller} is in position the {position} out of {len(value)}")
