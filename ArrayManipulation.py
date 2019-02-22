#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    # Initializing the array with n length.
    arr = [0] * n
    for value in queries:
        for index in range(value[0]-1, value[1]):
            arr[index] += value[2]
    return max(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
