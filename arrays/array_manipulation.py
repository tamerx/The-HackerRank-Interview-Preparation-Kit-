#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
        # Big O (N)
        res = [0]*(n+1) # we only really need one terminal row, since we're applying each pass to all rows below

        # loop through all the queries and apply the increments/decrements for each
        # Big O (M) (size of queires)
        for row in range(len(queries)):
                a = queries[row][0]
                b = queries[row][1]
                k = queries[row][2]

                res[a-1] += k # increment the starting position
                # this is where a loop would increment everything else between a & b by k
                # but instead of taking b-a steps, we take a constant 2 steps, saving huge on time
                res[b] -= k # decrement the position AFTER the ending position

        # now loop through res one time - Big O (N) (size of res)
        sm = 0 # running sum
        mx = 0 # maximum value found so far
        for i in range(len(res)):
                sm += res[i]
                if sm > mx:
                        mx = sm

        # total run time is Big O (2*N + M) >> Big O(N)
        return mx

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
