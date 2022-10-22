from collections import deque

def count_cheese(arr):
    sum = 0
    for i in range(n):
        sum += arr[i].count(1)
    return sum

def bfs(arr, n, m):
    queue = deque([])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue.append((0, 0))
    visited[0][0] = 1

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < n and 0 <= b < m:
                if arr[a][b] == 1: # cheese
                    arr[a][b] = 0
                    visited[a][b] = 1
                elif visited[a][b] == 0:
                    queue.append((a, b))
                    visited[a][b] = 1
                
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
last_cheese = 0
count = 0

while count_cheese(arr) != 0:
    last_cheese = count_cheese(arr)
    bfs(arr, n, m)
    count += 1

print(count)
print(last_cheese)
