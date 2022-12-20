import sys
INF = sys.maxsize

n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    dp = [INF for _ in range(2 * k + 1)]
    for i in range(0, n):
        dp[i] = n - i
        if i * 2 < len(dp):
            dp[i * 2] = dp[i]
    dp[n] = 0
    for i in range(n, len(dp) - 1):
        dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1)
        if dp[i] != INF and i * 2 < len(dp):
            dp[i * 2] = dp[i]

    print(dp[k])
