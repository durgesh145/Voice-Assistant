#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'problemSolving' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY v
#

def problemSolving(k, v):
    # Write your code here

 if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    v = list(map(int, input().rstrip().split()))

    result = problemSolving(k, v)

    fptr.write(str(result) + '\n')

    fptr.close()
