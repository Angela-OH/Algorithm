import sys
from collections import deque
input = sys.stdin.readline

def bfs(middle):
    queue = deque([])
    queue.append(x - 1)
    visited = [False for _ in range(n)]
    visited[x - 1] = True

    while queue:
        node = queue.popleft()
        if node == y - 1:
            return True
        for next_node, w in bridge[node]:
            if not visited[next_node] and w >= middle:
                queue.append(next_node)
                visited[next_node] = True

    return False

def binary_search(start, end):
    answer = 0
    while start <= end:
        middle = (start + end) // 2
        if bfs(middle):
            answer = middle
            start = middle + 1
        else:
            end = middle - 1
    return answer

n, m = map(int, input().split())
bridge = [[] for _ in range(n)]
min_weight = sys.maxsize
max_weight = 0
for i in range(m):
    a, b, c = map(int, input().split())
    if c < min_weight:
        min_weight = c
    if c > max_weight:
        max_weight = c
    bridge[a - 1].append((b - 1, c))
    bridge[b - 1].append((a - 1, c))

x, y = map(int, input().split())
print(binary_search(min_weight, max_weight))
