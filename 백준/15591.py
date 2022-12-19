import sys
from collections import deque
input = sys.stdin.readline

def bfs(index, k):
    queue = deque([])
    queue.append((index, sys.maxsize))
    visited = [0 for _ in range(n)]
    visited[index] = 1
    answer = 0

    while queue:
        node, dis = queue.popleft()
        if dis >= k:
            answer += 1
        for v in usado[node]:
            if visited[v[0]] == 0:
                queue.append((v[0], min(dis, v[1])))
                visited[v[0]] = 1

    return answer

n, q = map(int, input().split())
usado = [[] for _ in range(n)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    usado[a - 1].append([b - 1, c])
    usado[b - 1].append([a - 1, c])

for i in range(q):
    k, v = map(int, input().split())
    print(bfs(v - 1, k) - 1)