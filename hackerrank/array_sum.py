#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(ar):

    total_sum = 0
    total_sum = sum(ar)
    print(total_sum)
    return total_sum
    return sys.stdout.write(total_sum)


if __name__ == '__main__':
    result = simpleArraySum([1, 2, 3, 4, 10, 11])

    print(result)
