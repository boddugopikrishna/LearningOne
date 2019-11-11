array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
target = 83
'''
Binary Search algorithm steps:
1)Let min = 0 and max = n-1.
2)If max < min, then stop: target is not present in array. Return -1.
3)Compute guess as the average of max and min, rounded down (so that it is an integer).
4)If array[guess] equals target, then stop. You found it! Return guess.
5)If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
6)Otherwise, the guess was too high. Set max = guess - 1.
7)Go back to step 2.

'''
def BinarySearch(array,target):
    min = 0
    max = len(array) - 1
    if array[min] == target:
        return min
    elif array[max] == target:
        return max
    else:
        while max >= min:
            mid = (min + max) // 2
            if array[mid] == target:
                return mid
                break
            if array[mid] < target:
                min = mid + 1
            else:
                max = mid - 1
        else:
            return -1
print(BinarySearch(array,100))

#If max < min, then stop: target is not present in array. Return -1.




