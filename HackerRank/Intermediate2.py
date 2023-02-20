# Maximum Subarray Value
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarrayValue(arr):
    # Write your code here
    n = len(arr)
    e_sum, o_sum, e_o_sum = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
    for i in range(n):
        e_sum[i + 1] += e_sum[i]
        o_sum[i + 1] += o_sum[i]
        if i % 2 == 0:
            e_sum[i + 1] += arr[i]
        else:
            o_sum[i + 1] += arr[i]
        e_o_sum[i + 1] = e_sum[i + 1] - o_sum[i + 1]
    
    val = max(e_o_sum) - min(e_o_sum)
    return val * val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxSubarrayValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()