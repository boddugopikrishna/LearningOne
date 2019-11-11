numbers = [7,5,14,2,8,8,10,1,2,3]
max_number = []
for val in numbers:
    ind = numbers.index(val)
    for number in numbers[ind+1:]:
        max_number.append(val* number)
print(max(max_number))