import sys
input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(x, y):
    global answer
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] != -1: #  이미 탐색한 적이 있음
        return dp[x][y]
    dp[x][y] = 0
    height = graph[x][y]
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if 0 <= new_x < m and 0 <= new_y < n:
            if graph[new_x][new_y] < height:
                dp[x][y] += dfs(new_x, new_y)
    return dp[x][y]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
answer = 0

print(dfs(0, 0))
