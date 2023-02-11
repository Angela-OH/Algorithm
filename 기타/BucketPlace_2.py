import sys
INF = sys.maxsize

def solution(n):
    dp = [INF for _ in range(n + 1)]
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

print(solution(8))
print(solution(10))
print(solution(11))
print(solution(20))
print(solution(100))