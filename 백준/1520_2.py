import sys
input = sys.stdin.readline

def dfs(i, j):
    if i == m - 1 and j == n - 1:
        return 1
    
    if dp[i][j] != -1: # 이전에 계산해둔 값 재사용
        return dp[i][j]

    dp[i][j] = 0

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + di, j + dj
        if (0 <= new_i < m) and (0 <= new_j < n):
            if loc[new_i][new_j] < loc[i][j]:
                dp[i][j] += dfs(new_i, new_j)

    return dp[i][j]
    
m, n = map(int, input().split())
loc = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)] # 1은 가능, -1은 불가능
answer = 0

dfs(0, 0)

print(dp[0][0])