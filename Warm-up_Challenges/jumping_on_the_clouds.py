#!/bin/python3

import os


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(lst):
    x = 0
    count = 0
    k = 0
    while k <= len(lst) - 1:

        if k + 1 >= len(lst):
            break
        if k + 2 >= len(lst):
            count += 1
            break

        if lst[k + 2] == 0:
            k += 2
            count += 1
        else:
            k += 1
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
