#!/bin/python3

import os

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = 0
    orange = 0
    for i in range(len(apples)):
        temp = a + apples[i]
        if(temp in range(s,t+1)):
            apple+=1
    for i in range(len(oranges)):
        temp = b + oranges[i]
        if(temp in range(s,t+1)):
            orange+=1
    print(apple)
    print(orange)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
