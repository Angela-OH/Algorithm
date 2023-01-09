n = int(input())

if n % 2 != 0: # 주어진 타일로 채울 수 x
    print(0)
    exit()

dp = [0 for _ in range(n + 1)]
dp[0], dp[1], dp[2] = 1, 1, 3

for i in range(4, n + 1, 2):
    dp[i] += (dp[i - 2] * dp[2])
    for j in range(i - 4, -1, -2):
        dp[i] += (dp[j] * 2)
print(dp[n])
