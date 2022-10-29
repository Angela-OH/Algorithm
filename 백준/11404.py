import sys

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or i == j:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = sys.maxsize
route = [[] for _ in range(n)]
graph = [[INF for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c > graph[a - 1][b - 1]:
        c = graph[a - 1][b - 1]
    route[a - 1].append((b - 1, c))
    graph[a - 1][b - 1] = c

floyd_warshall()

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()