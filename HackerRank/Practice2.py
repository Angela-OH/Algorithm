# Prefix Scores
#!/bin/python3

import math
import os
import random
import re
import sys


 
#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getPrefixScores(arr):
    # Write your code here
    mod = 10 ** 9 + 7
    n = len(arr)
    answer = [0 for _ in range(n + 1)]
    prev = 0
    
    for i in range(n): # put default answer
        prev += arr[i]
        answer[i + 1] = answer[i] + prev
    
    prev = 0
    for i in range(n): # consider maximum
        prev = max(prev, arr[i])
        answer[i + 1] += (i + 1) * prev
        answer[i + 1] %= mod 
        
    return answer[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getPrefixScores(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
