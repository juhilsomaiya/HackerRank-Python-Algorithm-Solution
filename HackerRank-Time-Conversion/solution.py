#!/bin/python3

import os
import sys

def timeConversion(s):
    #
    # Write your code here.
    #
    print(str(s))
    time = (s.split(":"))
    ampm = time[2][2:4]
    if ampm == "PM":
        if time[0] != "12":
            time[0]=int(int(time[0])+12)
            time[0] = str(time[0])
    elif ampm == "AM":
        if time[0] == "12":
            time[0] = "00"
        
    ntime = ':'.join(time)
    print(str(ntime))
    return str(ntime[:-2])
    
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
