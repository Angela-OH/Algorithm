from collections import deque

def solution(maps):
    queue = deque([])
    queue.append((0, 0, 1))
    m, n = len(maps), len(maps[0]) # 세로, 가로
    visited = [[0 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while queue:
        x, y, level = queue.popleft()
        if x == (m - 1) and y == (n - 1):
            return level
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n:
                if maps[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = 1
                    queue.append((new_x, new_y, level + 1))
    return -1