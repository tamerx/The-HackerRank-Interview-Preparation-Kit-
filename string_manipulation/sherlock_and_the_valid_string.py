#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the isValid function below.

def isValid(s):
    MyList = list(s)
    ListCount = Counter(MyList)
    print(ListCount)
    if (len(set(ListCount.values())) == 1):
        return "YES"
    else:
        k = len(ListCount.keys())
        v = set(ListCount.values())
        x1 = v.pop()
        x2 = v.pop()
        if sum(ListCount.values()) - 1 == k * x1:
            return "YES"
        if sum(ListCount.values()) - 1 == x2 * (k - 1):
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
