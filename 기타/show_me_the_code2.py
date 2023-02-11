import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    queue = deque([])
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            new_x, new_y = x + dx, y + dy
            if new_x < 0:
                new_x = n - 1
            elif new_x >= n:
                new_x = 0
            if new_y < 0:
                new_y = m - 1
            elif new_y >= m:
                new_y = 0
            if arr[new_x][new_y] == 0 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            answer += 1
            bfs(i, j)

print(answer)