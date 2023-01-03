n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    dp[i][0] = dp[i - 1][1] # 0은 1의 계단수
    dp[i][9] = dp[i - 1][8] # 9는 8의 계단수

    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n - 1]) % 1000000000)
