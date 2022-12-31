t = int(input())
for i in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m + 1)]
    dp[0] = 1

    for a in range(n):
        for b in range(coin[a], m + 1):
            dp[b] += dp[b - coin[a]]

    print(dp[m])