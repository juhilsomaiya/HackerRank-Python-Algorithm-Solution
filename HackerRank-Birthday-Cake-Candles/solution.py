#!/bin/python3

import math
import os
import random
import collections
import re
import sys

def birthdayCakeCandles(ar):
    return (max(collections.Counter(ar).values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
