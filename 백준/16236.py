import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
time = 0
size = 2
fish = 0
fish_total = 0
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
        elif graph[i][j] != 0:
            fish_total += 1

#print(x, y)

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited = [[0] * n for j in range(n)]
    da = [-1, 0, 0, 1]
    db = [0, -1, 1, 0]
    candidate = []

    while queue:
        a, b, time = queue.popleft()
        visited[a][b] = 1
        for i in range(4):
            a1, b1 = a + da[i], b + db[i]
            if (0 <= a1 < n) and (0 <= b1 < n) and (visited[a1][b1] == 0):
                if 0 < graph[a1][b1] < size:
                    #print((a1, b1, time))
                    candidate.append((a1, b1, time + 1))
                elif graph[a1][b1] == 0 or graph[a1][b1] == size:
                    visited[a1][b1] = 1
                    queue.append((a1, b1, time + 1))
    
    if not candidate:
        return (0, 0, 0)
    candidate.sort(key = lambda x: (x[2], x[0], x[1]))
    return candidate[0]

while fish_total:
    a, b, min_time = bfs(x, y)
    if min_time == 0:
        break
    graph[x][y], graph[a][b] = 0, 9
    time += min_time
    fish += 1
    fish_total -= 1
    if fish == size:
        size += 1
        fish = 0
    x, y = a, b

print(time)