from collections import deque

def bfs(status, grid, n, m, i, j, dx, dy, status_val, grid_val):
    queue = deque([])
    queue.append((i, j))
    status[i][j] = status_val
    while queue:
        x, y = queue.pop()
        for k in range(len(dx)):
            new_x, new_y = x + dx[k], y + dy[k]
            if (0 <= new_x < n) and (0 <= new_y < m):
                if status[new_x][new_y] == 0 and grid[new_x][new_y] == grid_val:
                    status[new_x][new_y] = status_val
                    queue.append((new_x, new_y))

def solution(grid):
    answer = 0
    n = len(grid)
    m = len(grid[0])
    status = [[0 for _ in range(m)] for _ in range(n)] # 1은 선, -1은 아무것도 x
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1] # 대각선
    dx2, dy2 = [-1, 1, 0, 0], [0, 0, 1, -1] # 상하좌우

    # 선 찾기 (1)
    for i in range(n):
        for j in range(m):
            if status[i][j] == 0 and grid[i][j] == '#':
                bfs(status, grid, n, m, i, j, dx, dy, 1, '#')

    # 도형에 속하지 않는 영역 찾기 (-1)
    for i in range(m):
        if status[0][i] == 0:
            bfs(status, grid, n, m, 0, i, dx2, dy2, -1, '.')
        if status[n - 1][i] == 0:
            bfs(status, grid, n, m, n - 1, i, dx2, dy2, -1, '.')

    for i in range(n):
        if status[i][0] == 0:
            bfs(status, grid, n, m, i, 0, dx2, dy2, -1, '.')
        if status[i][m - 1] == 0:
            bfs(status, grid, n, m, i, m - 1, dx2, dy2, -1, '.')

    # 선 (1)과 도형 (0) 개수 구하기
    for i in range(n):
        for j in range(m):
            if status[i][j] != -1:
                answer += 1

    return answer