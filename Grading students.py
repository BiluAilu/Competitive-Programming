

import math
import os
import random
import re
import sys

#Completed functions

def gradingStudents(grades):
    for i in range(len(grades)):
        nextMultiple = (grades[i] - (grades[i] % 5))+ 5
        if (nextMultiple - grades[i]) < 3:
            if grades[i] >= 38:
                grades[i] = nextMultiple
            else:
                continue
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()