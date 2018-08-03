#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    result = 0
    for i in range(len(ar)):
        result = result + ar[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
