def solution(land):
    n = len(land)
    lands = [[0 for _ in range(4)]]
    dp = [[0 for _ in range(4)] for _ in range(n + 1)]
    lands.extend(land)

    for i in range(1, n + 1):
        for j in range(4):
            result = max(dp[i - 1][:j] + dp[i - 1][j + 1:])
            dp[i][j] = lands[i][j] + result
    answer = max(dp[n])
    return answer