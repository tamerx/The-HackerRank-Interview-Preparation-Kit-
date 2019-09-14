#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    arr,count=bubbleSort(a)
    print("Array is sorted in {0} swaps.".format(count))
    print("First Element: {0}".format(arr[0]))
    print("Last Element: {0}".format(arr[-1]))




def bubbleSort(arr):
    n = len(arr)
    count = 0

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j],
                count += 1

    return arr, count

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
