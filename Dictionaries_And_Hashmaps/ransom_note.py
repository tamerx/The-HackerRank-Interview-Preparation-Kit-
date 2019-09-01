#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for str_note in note:
        if str_note in magazine:
            magazine.pop(magazine.index(str_note))
        else:
            return "No"

    return "Yes"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(sorted(magazine), sorted(note)))
