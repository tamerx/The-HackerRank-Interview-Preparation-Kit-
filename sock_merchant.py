#!/bin/python3

import os


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    while len(ar) > 0:
        l = ar.pop(0)

        if l in ar:
            index = ar.index(l)
            ar.pop(index)
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
