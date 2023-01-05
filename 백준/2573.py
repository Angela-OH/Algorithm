import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    if len(ice_location) == 0:
        return 0
    x, y = ice_location[0][0], ice_location[0][1]
    queue = deque([])
    queue.append((x, y))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            new_x, new_y = x + dx[k], y + dy[k]
            if 0 <= new_x < n and 0 <= new_y < m:
                if ice[new_x][new_y] != 0 and not visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    count += 1

    if count == len(ice_location):
        return 1
    else:
        return 2

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
decrease = [[0 for _ in range(m)] for _ in range(n)]
ice_location = []
year = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if ice[i][j] != 0:
            ice_location.append((i, j))

while True:
    if len(ice_location) == 0 or bfs() == 2:
        break

    year += 1

    # 높이 얼마나 감소시킬지 조사
    for index in range(len(ice_location)):
        x, y = ice_location[index][0], ice_location[index][1]
        count = 0
        for u in range(4):
            new_x, new_y = x + dx[u], y + dy[u]
            if 0 <= new_x < n and 0 <= new_y < m:
                if ice[new_x][new_y] == 0:
                    count += 1
        decrease[x][y] = count

    # 높이 감소시키기
    index = 0
    while True:
        if index >= len(ice_location):
            break
        x, y = ice_location[index][0], ice_location[index][1]
        if ice[x][y] > decrease[x][y]:
            ice[x][y] -= decrease[x][y]
            index += 1
        else:
            ice[x][y] = 0
            del ice_location[index]

if len(ice_location) == 0:
    print(0)
else:   
    print(year)