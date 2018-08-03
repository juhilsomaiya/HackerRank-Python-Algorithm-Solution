#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    primary=0
    secondary=0 
    n = len(arr)
    print(n)
    for i in range(n):
         for j in range(n):
             if i==j:
                 primary = primary + arr[i][j]
             if i==n-j-1:
                 secondary = secondary + arr[i][j]
    return abs(primary-secondary)
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
