#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            plus = plus + 1
        elif arr[i] < 0:
            minus = minus + 1
        else:
            zero = zero + 1 
    print("{0:.6f}".format(plus/len(arr)))
    print("{0:.6f}".format(minus/len(arr)))
    print("{0:.6f}".format(zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
