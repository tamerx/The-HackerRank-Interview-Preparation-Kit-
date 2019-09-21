#!/bin/python3

import math
import os
import random
import re
import sys

sys.getsizeof([None] * (2**20)) # 8388680

def myFunc(k):
    if len(k) == 1 or (len(set(k)) == 2 and k == k[::-1]) or (len(set(k)) == 1 and len(k) > 1):
        return True


def substrCount(n, s):
    myList = list(s)
    k2 = []
    newList = [[myList[j:i] for i in range(j, len(myList) + 1) if myList[j:i] != ""] for j in range(0, len(myList) + 1)]
    for k in newList:
        k2.extend(k)
    k2 = list(filter(myFunc, list(filter(lambda x: x != [], k2))))
    return len(k2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
