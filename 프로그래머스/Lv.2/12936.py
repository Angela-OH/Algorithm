def factorial(n):
    dp = [1 for i in range(n + 1)]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i
    return dp
def solution(n, k):
    answer = []
    dp = factorial(n)
    visited = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        a = (k - 1) // dp[i] + 1
        count = 0
        for j in range(n):
            if visited[j] == 1:
                continue
            else:
                count += 1
            if count == a:
                visited[j] = 1
                answer.append(j + 1)
                break
        b = (k - 1) % dp[i] + 1
        k = b
    return answer