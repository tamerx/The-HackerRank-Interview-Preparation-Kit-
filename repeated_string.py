#!/bin/python3

import os


# Complete the repeatedString function below.
def repeatedString(s, k):
    x = s.count("a")
    if x == 0:
        return 0
    elif len(s) == 1:
        return x * k
    else:
        return (x * (k // len(s))) + s[0:(k % len(s))].count("a")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
