#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # If it is less than 0 it is negative, 
    # If it is greater than 0 it is positive.
    # If it is equal to 0 is is also zero, but counted towards the negative.
    # a list or array of size n, with a space in between each number.
    positive = 0
    negative = 0
    count = 0
    zeros = 0

    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        elif i == 0:
            zeros += 1
        
        count += 1
    positive_ratio = positive / count
    negative_ratio = negative / count
    zero_ratio = (count - positive - negative) / count
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
    return positive, negative

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
