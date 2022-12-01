#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    company_name = input()
    dic = {}
    for c in company_name:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    group = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
    for g in group[:3]:
        print("{} {}".format(g[0], g[1]))