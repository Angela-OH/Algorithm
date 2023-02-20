# Multi Dimensional Selection
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

INF = sys.maxsize
k = INF
res = []

def find(arr, n, m, h, min_v, max_v, i):
    global k
    if i == n:
        val = max_v - min_v
        if val <= k:
            if val < k:
                k = val
                res.clear()
            res.append((min_v, max_v))
        return
    
    gap = INF
    left, right = 0, 0
    for j in range(0, m - h):
        v = max(abs(max_v - arr[i][j]), abs(arr[i][j + h] - min_v))
        
        if v <= gap:
            gap = v
            left, right = j, j + h
       
    find(arr, n, m, h, min(min_v, arr[i][left]), max(max_v, arr[i][right]), i + 1)

def getMaxProduct(arr):
    # Write your code here
    min_v, max_v = INF, -INF
    cnt, n, m = 0, len(arr), len(arr[0])
    l, r = math.ceil(m/2) - 1, m - math.ceil(m/2)
    h = math.ceil(m/2) - 1
    
    for a in arr:
        a.sort()
    
    for i in range(0, m - h):
        find(arr, n, m, h, arr[0][i], arr[0][i + h], 1)
    # select left (1st row)
    #find(arr, n, l, r, arr[0][0], arr[0][l], 1)
 
    # select right (1st row)
    #find(arr, n, l, r, arr[0][r], arr[0][-1], 1)
    
    for r in res:
        sum = 0
        for ar in arr:
            for a in ar:
                if r[0] <= a <= r[1]:
                    sum += 1
                if a > r[1]: break
        cnt = max(cnt, sum)
    
    return k * cnt

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
