#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(*arr):
    i = 0
    j = 0
    arr_diag1 = 0
    arr_diag2 = 0
    total_diff = 0
    for i, row in enumerate(arr):
        arr_diag1 += row[i][i+1]  # Primary diagonal
        arr_diag2 += row[len(arr) - 1 - i]  # Secondary diagonal
        print(arr_diag1, arr_diag2)

        
        print(arr_diag1, arr_diag2)
    total_diff = abs(arr_diag1 - arr_diag2)
    
    return total_diff

mydiagd = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
print(mydiagd)

# I need the first pos 0,0 and I need the 1,1, and 2, 2 then 0,2 and 1,1 and 2,0
# so how could I get that?

# i = 0 j = 0 I can iterate through the first to get the Diagonals
mydiagd2 = diagonalDifference([3],[11, 2, 4],[4, 5, 6],[10, 8, -12])
print(mydiagd2)