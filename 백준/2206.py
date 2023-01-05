import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    visited = [[0 for _ in range(m)] for _ in range(n)] # 미방문: 0, 벽을 부수지 않고 방문:1, 벽을 부수고 방문: 2
    queue = deque([])
    visited[x][y] = 1
    queue.append((x, y, 1, 0)) # 세번째 인자는 이동 거리, 네번째 인자는 벽을 부순 횟수
    
    while queue:
        i, j, dis, cnt = queue.popleft()
        if i == n - 1 and j == m - 1:
            return dis
        for k in range(4):
            new_i, new_j = i + di[k], j + dj[k]
            if 0 <= new_i < n and 0 <= new_j < m:
                if graph[new_i][new_j] == 0:
                    if cnt == 0 and visited[new_i][new_j] != 1:
                        queue.append((new_i, new_j, dis + 1, cnt))
                        visited[new_i][new_j] = 1
                    elif cnt == 1 and visited[new_i][new_j] == 0:
                        queue.append((new_i, new_j, dis + 1, cnt))
                        visited[new_i][new_j] = 2
                elif graph[new_i][new_j] == 1 and cnt == 0: # 벽을 부술 수 있음
                    queue.append((new_i, new_j, dis + 1, cnt + 1))
                    visited[new_i][new_j] = 2

    return -1

n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    t = input()
    for j in range(m):
        graph[i][j] = int(t[j])

print(bfs(0, 0))