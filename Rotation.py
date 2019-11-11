#!/bin/python3

import math
import os
import random
import re
import sys


def roation(rotation_list, rotation_factor):
    for val in range(rotation_factor):
        j = 0
        updated_list = []
        while j < len(rotation_list) - 1:
            updated_list.append(rotation_list[j + 1])
            j = j + 1
        updated_list.append(rotation_list[0])
        rotation_list = updated_list
        # ' '.join([str(v) for v in L])
    return " ".join(list(map(str, rotation_list)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result = roation(a, d)

    fptr.write(str(result))

    fptr.close()
