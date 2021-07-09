#!/bin/python

import math
import os
import random
import re
import sys


# write your code here

def avg(n=[], total=0):
    n.split()
    for integer in n:
        if integer in range(-100, 101):
            total += integer
    average = total / len(n)
    return f"{average:.2f}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = map(int, raw_input().split())
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
