#!/bin/python3

import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    print (num)
    

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
