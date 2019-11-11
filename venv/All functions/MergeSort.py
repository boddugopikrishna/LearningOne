
def sorted_array(array,output=None):
    if output == None:
        output = []
    if len(array) > 0:
        output.append(min(array))
        array.remove(min(array))
        return sorted_array(array,output)
    return output

a = [4,3,7,1,8,2,9,5,6]
mid_array = len(a) // 2
array1 = sorted_array(a[:mid_array])
print(array1)

array2 = sorted_array(a[mid_array:])
print(array2)
def mergesort(array1,array2):
    m = len(array1)
    n = len(array2)
    i = 0
    j = 0
    merge_sorted = []

    while i + j < m + n:
        if i == m :
            merge_sorted.append(array2[j])
            j += 1
        elif j == n :
            merge_sorted.append(array1[i])
            i += 1
        elif array1[i] <= array2[j]:
            merge_sorted.append(array1[i])
            i += 1
        else:
            merge_sorted.append(array2[j])
            j += 1
    return merge_sorted

print(mergesort(array1,array2))





