import sys
from collections import deque

def bfs(m, x, y):
    max = 0
    queue = deque([])
    visited = [[0 for i in range(y)] for j in range(x)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(x):
        for j in range(y):
            if m[i][j] == "L" and visited[i][j] == 0:
                queue.append((i, j, 0))
                visited[i][j] = 1
                while queue:
                    a, b, level = queue.popleft()
                    for k in range(4):
                        a2, b2 = a + dx[k], b + dy[k]
                        if (0 <= a2 < x) and (0 <= b2 < y):
                            if m[a2][b2] == 'L' and visited[a2][b2] == 0:
                                queue.append((a2, b2, level + 1))
                                visited[a2][b2] = 1
                                if level + 1 > max:
                                    max = level +1
                visited = [[0 for i in range(y)] for j in range(x)]
                
    return max

x, y = map(int, sys.stdin.readline().split())
m = [list(sys.stdin.readline().strip()) for _ in range(x)]

print(bfs(m, x, y))