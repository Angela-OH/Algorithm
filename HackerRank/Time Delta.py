#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time = [t1.split(), t2.split()]
    info = []
    month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
        'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    sec = 0
    
    for i in range(2):
        time[i][2] = str(month[time[i][2]])
        info.append(datetime.strptime(' '.join(time[i][1:5]), '%d %m %Y %H:%M:%S'))
    sec += int((info[0] - info[1]).total_seconds())
    
    print(sec)
    
    for i in range(2):
        hour = int(time[i][5][1:3])
        mins = int(time[i][5][3:])
        seconds = 60 * 60 * hour + 60 * mins
        print(seconds)
        if time[i][5][0] == '+':
            if i == 0:
                sec -= seconds
            else:
                sec += seconds
        else:
            if i == 0:
                sec += seconds
            else:
                sec -= seconds

    return str(abs(sec))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
