'''students = [5.5,6.5,6.8,7.3,7.8,9.9,7.4]
i = len(students)
count = 0
groups = []
while i != 0:
    initial_student = students[0]
    print ("initial Student :{}".format(initial_student))
    initil_position = 0
    group = []
    print("initial group :{}".format(group))
    for val in students[students.index(initial_student) + 1 :]:
        if val - initial_student >= 1:
            group.append(initial_student)
            initial_student = val
            initil_position = students.index(val)
    group.append(initial_student)
    print("Final group :{}".format(group))
    groups.append(group)
    print("Final list of groups :{}".format(groups))
    for val in group:
        students.remove(val)
    print("Final Students list :{}".format(students))
    i = len(students)
    print("Length of students:{}".format(i))
for group in groups:
    if len(group) >= 2:
        count = count + 1
        print("{} Group/Groups having 2 or more numbers and their group members {} ".format(count,group))
#print(initil_position)
#print(initial_student)
#print(group)'''
numbers = [4,6,7,9,5]

'''def largest_number(numbers):
    i = len(numbers)
    max_numbers =[]
    while i > 0:
        max_number = 0
        for val in numbers:
            if val >= max_number:
                max_number = val
        max_numbers.append(max_number)
        numbers.remove(max_number)
        i = len(numbers)
    return "".join(map(str,max_numbers))

print(largest_number(numbers))'''


money = 140
count = 0
iteration = 0
while money > 0:
    print ("Money {} at iteration {}".format(money,iteration))
    if money > 10 and money % 10 != 0:
        count = count + (money // 10)
        print("Count of coins at condition : money > 10 and money % 10 != 0 is  {}".format(count))
        iteration = iteration + 1
        money = money - ((money // 10)* 10 )

    elif money > 10 and money % 10 == 0:
        count = count + ((money // 10) - 1)
        print("Count of coins at condition : money > 10 and money % 10 == 0 is {}".format(count))
        iteration = iteration + 1
        money = money - (((money // 10) - 1)* 10 )

    elif money <= 10 and money > 5:
        iteration = iteration + 1
        count = count + 1
        print("Count of coins at condition : money <= 10 and money > 5 is {}".format(count))
        money = money - 5
    elif money <= 5 and money > 0:
        iteration = iteration + 1
        count = count + money * 1
        print("Count of coins at condition : money <= 5 and money > 0  is {}".format(count))
        money = money - (money * 1)
    else:
        iteration = iteration + 1
        print(count)
print(count)



