import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(i, j):
    global answer

    if dp[i][j] != 0:
        return dp[i][j]

    dp[i][j] = 1

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + di, j + dj
        if (0 <= new_i < n) and (0 <= new_j < n):
            if forest[new_i][new_j] > forest[i][j]:
                dp[i][j] = max(dp[i][j], dfs(new_i, new_j) + 1)

    return dp[i][j]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)