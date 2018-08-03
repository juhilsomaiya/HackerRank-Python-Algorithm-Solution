#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    x = sum(map(int,arr))
    print ((x-(max(arr))), (x-(min(arr))))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
