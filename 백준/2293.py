n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    coin = int(input())
    for j in range(k + 1):
        if coin > j:
            continue
        dp[j] += dp[j - coin]

print(dp[k])