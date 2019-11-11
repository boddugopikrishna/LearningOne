n = 10
queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    zero_indexed_list = [0 for val in range(n)]
    for query in queries:
        while query[0] <= query[1]:
            zero_indexed_list[query[0] - 1 ] = zero_indexed_list[query[0] - 1 ] + query[2]
            query[0] = query[0] + 1
    return max(zero_indexed_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = sys.stdin.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

