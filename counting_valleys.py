#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    count2 = 0
    for str in s:
        if str == "U":
            count2 += 1
        if str == "D":
            count2 -= 1

        if count2 == 0 and str == "U":
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
