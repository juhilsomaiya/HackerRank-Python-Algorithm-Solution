#!/bin/python3

import os
import sys

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38 and grades[i] %5 >=3:
            while grades[i] %5 !=0:
                grades[i] = grades[i] + 1
    return grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
