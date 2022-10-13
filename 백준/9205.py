import sys
from collections import deque

min, max = -32768, 32767

def distance(a, b):
    return 1000 >= abs(a[0] - b[0]) + abs(a[1] - b[1])

def dfs(house, con, dest, n):
    queue = deque([(house[0], house[1])])
    visited = [0] * n

    while queue:
        x, y = queue.popleft()
        
        if distance([x, y], dest):
            return 1
        
        for i in range(n):
            a, b = con[i]
            if visited[i] == 0:
                if distance((x, y), (a, b)):
                    visited[i] = 1
                    queue.append((a, b))
        
    return 0

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    house = list(map(int, sys.stdin.readline().rstrip().split()))
    con = []
    for _ in range(n):
        con.append(list(map(int, sys.stdin.readline().rstrip().split())))
    dest = list(map(int, sys.stdin.readline().rstrip().split()))

    if dfs(house, con, dest, n) == 1:
        print("happy")
    else:
        print("sad")