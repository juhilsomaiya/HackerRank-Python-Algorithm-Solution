#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def migratoryBirds(arr):
    count = Counter(arr).most_common(5)
    return count[0][0]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
