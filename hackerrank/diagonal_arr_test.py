#!/bin/python3

import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    arr = ([3],[11, 2, 4],[4, 5, 6],[10, 8, -12])
    #i = 0
    j = 0
    arr_diag1 = 0
    arr_diag2 = 0
    total_diff = 0
    for i, row in enumerate(arr):
        if len(row) <= 1:
            continue
        else:
                
            arr_diag1 += row[j]  # Primary diagonal
            arr_diag2 += row[len(row) - 1 - j]  # Secondary diagonal
            
            j += 1
            print(arr_diag1, arr_diag2)

            
    return total_difference(arr_diag1, arr_diag2)
        
def total_difference(arr1, arr2):
    total_diff = abs(arr1 - arr2)
    return total_diff



        
mydiagd2 = ([3],[11, 2, 4],[4, 5, 6],[10, 8, -12])
print(mydiagd2)
result = diagonalDifference(mydiagd2)
print(result)