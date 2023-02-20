#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxProduct' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def getMaxProduct(arr):
    # Write your code here
    n, m = len(arr), len(arr[0])
    h = math.ceil(m / 2)
    cnt = [0 for _ in range(n)] # check count per row
    info = []
    k, num, row = sys.maxsize, 0, n
    
    for i in range(n):
        for a in arr[i]:
            info.append((a, i))
    info.sort()
    
    j = 0
    for i in range(len(info)): # start point
        while j < len(info) and row > 0: # sliding
            cnt[info[j][1]] += 1
            if (cnt[info[j][1]] == h): row -= 1
            j += 1
        if row == 0: # satisfy the requirements
            tmp = info[j - 1][0] # latest val
            while j < len(info) and info[j][0] == tmp:
                cnt[info[j][1]] += 1
                j += 1
            val = info[j - 1][0] - info[i][0]
            if val < k:
                k = val
                num = j - i
            elif val == k:
                num = max(num, j - i)
        
        # undo
        if cnt[info[i][1]] == h: 
            row += 1
        cnt[info[i][1]] -= 1        
                    
    return k * num
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    result = getMaxProduct(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
