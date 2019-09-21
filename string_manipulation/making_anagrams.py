#!/bin/python3

import math
import os
import random
import re
import sys

def string_intersect(str1, str2):
    # using naive method to
    # get string intersection
    res = ""
    for i in str1:
        if i in str2: # and not i in res:
            res += i
    return res

# Complete the makeAnagram function below.
def makeAnagram(str1, str2):
    res = string_intersect(str1, str2)
    # res = set(str1).intersection(str2)


    res = list(res)
    res2 = res.copy()
    print(res)
    count = 0
    for str_1 in str1:
        if str_1 not in res:
            count += 1
        elif str_1 in res:
            # count += 1
            res.remove(str_1)
    
    for str_2 in str2:
        if str_2 not in res2:
            count += 1
        elif str_2 in res2:
            # count += 1
            res2.remove(str_2)
    return(count+len(res2))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
