#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY val
#  2. UNWEIGHTED_INTEGER_GRAPH t
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#
def getMinCost(val, t_nodes, t_from, t_to):
    # Write your code here
    graph = [[] for _ in range(t_nodes + 1)] 
    leaf = []
    answer = 0
    
    for i in range(t_nodes - 1):
        graph[t_to[i]].append(t_from[i])
        graph[t_from[i]].append(t_to[i])
    
    for i in range(1, t_nodes + 1):
        val[i - 1] %= 2
        if len(graph[i]) == 1: leaf.append(i)
   
    while leaf:
        n_leaf = []
        for l in leaf:
            if len(graph[l]) == 0:
                return answer
            p = graph[l][0]
            graph[p].remove(l)
            if val[l - 1] == 1:
                answer += 1
                val[l - 1] = 0
                val[p - 1] = 1 - val[p - 1]
            
            if len(graph[p]) == 1:
                n_leaf.append(p)
        leaf = n_leaf[:]
        
    return answer

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    val_count = int(input().strip())

    val = []

    for _ in range(val_count):
        val_item = int(input().strip())
        val.append(val_item)

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    result = getMinCost(val, t_nodes, t_from, t_to)

    fptr.write(str(result) + '\n')

    fptr.close()
