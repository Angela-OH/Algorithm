n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = triangle[0][0]

for i in range(n - 1):
    for j in range(i + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

print(max(dp[n - 1]))