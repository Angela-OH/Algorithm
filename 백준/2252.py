import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
enter = [0 for _ in range(n)]
queue = deque([])
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    enter[b - 1] += 1

for i in range(n):
    if enter[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    answer.append(node)
    for g in graph[node]:
        enter[g] -= 1
        if enter[g] == 0:
            queue.append(g)

for i in range(n):
    print(answer[i] + 1, end = ' ')
    