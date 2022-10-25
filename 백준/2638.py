from collections import deque

def count_cheese():
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                count += 1
    return count

def cheese():
    queue = deque([])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if arr[new_x][new_y] == 1:
                    visited[new_x][new_y] += 1
                    continue
                if visited[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = 1
        
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                arr[i][j] = 0

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
time = 0

while count_cheese():
    cheese()
    time += 1

print(time)
