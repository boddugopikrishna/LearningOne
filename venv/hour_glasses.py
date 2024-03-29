#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    i = 0
    j = 0
    hour_glasses_list = []
    hours_glasses_val = []
    while i <= 3:
        while j <= 3:
            val = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                  arr[i + 2][j + 2]
            hour_glasses_list.append(
                [arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i + 1][j + 1], arr[i + 2][j], arr[i + 2][j + 1],
                 arr[i + 2][j + 2]])
            hours_glasses_val.append(val)
            j = j + 1
        i = i + 1
        j = 0
    return max(hours_glasses_val)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
