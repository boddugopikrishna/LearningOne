lst = [x for x in range(1,11)]

# Append - Add an item to  the end of the list
lst.append(12)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
lst.append(13)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12,13]
lst.pop()
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
print(lst)

# Extend - Extend the list by appending all the items from
#iterables
lst2 = [x for x in range(13,21)]
lst.extend(lst2)


# Insert - Insery an Item at given position
ind = lst.index(10)
lst.insert(ind + 1 , 11)

# Remove - Removes the first item from the list whose
# value is eqaul to x
lst.append(1)
lst.remove(1)

#print(lst[-1:] + lst[:-1])

#pop - Removes the item at given posiiton in the list
#if no index is specifided ,removes and returns last item in the list
#print(lst.pop(len(lst)-1))



