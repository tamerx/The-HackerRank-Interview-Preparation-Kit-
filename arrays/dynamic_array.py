#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    myArr = []
    myArrGlb = []
    for i in range(0, 4):
        for j in range(0, 4):
            myArr.clear()
            myArr.append(arr[i][j])
            myArr.append(arr[i][j + 1])
            myArr.append(arr[i][j + 2])
            myArr.append(arr[i + 1][j + 1])
            myArr.append(arr[i + 2][j])
            myArr.append(arr[i + 2][j + 1])
            myArr.append(arr[i + 2][j + 2])
            myArrGlb.append(list(myArr))

    return (max([sum(lst) for lst in myArrGlb]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
