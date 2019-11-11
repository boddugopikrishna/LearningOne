numbers = [1,2,6,9,23,73,43,65,32,4]
'''max_number = 0
for val in numbers:
    if val > max_number:
        max_number = val
print(max_number)'''


def max_numbers(numbers_list):
    max_number = 0
    for val in numbers:
        if val > max_number:
            max_number = val
    return max_number
#max_val = numbers.pop()
#print(max_val)
bubble_sorted_list = []
#max_val = max_numbers(numbers)
#print(max_val)
#bubble_sorted_list.append(max_val)
#print(bubble_sorted_list)


def bubble_sort(number_list):
    #bubble_sorted_list = []
    max_val = max_numbers(numbers)
    bubble_sorted_list.append(max_val)
    number_list.remove(max_val)
    if len(number_list) != 0:
        bubble_sort(number_list)
    return bubble_sorted_list
sort_list = bubble_sort(numbers)
print(sort_list)


