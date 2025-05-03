#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    Alice = 0
    Bob = 0
    i= 0
    j= 0
    neither = 0
    
    for i, j in list(zip(a, b)):
        
        print(i, j)
        if i > j:
            Alice += 1
        elif i < j:
            Bob += 1
        elif i == j:
            neither += 1
    return [Alice, Bob]
    # Write your code here, b_score]



if __name__ == '__main__':
    compareTriplets([1, 2, 3], [3, 2, 1])