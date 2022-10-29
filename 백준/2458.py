import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
count = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1

for a in range(n):
    for b in range(n):
        for c in range(n):
            if graph[b][a] == 1 and graph[a][c] == 1:
                graph[b][c] = 1

for a in range(n):
    sum = 0
    for b in range(n):
        sum += graph[a][b] + graph[b][a]
    if sum == n - 1:
        count += 1

print(count)


