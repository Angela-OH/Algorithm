# File Renaming
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

def renameFile(newName, oldName):
    # Write your code here
    n, m = len(newName), len(oldName)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, m):
            dp[i + 1][j + 1] += dp[i + 1][j]
            if newName[i] == oldName[j]:
                if i == 0 or j == 0: 
                    dp[i + 1][j + 1] += 1
                else:
                    dp[i + 1][j + 1] += dp[i][j] 
    return dp[n][m] % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    newName = input()

    oldName = input()

    result = renameFile(newName, oldName)

    fptr.write(str(result) + '\n')

    fptr.close()

