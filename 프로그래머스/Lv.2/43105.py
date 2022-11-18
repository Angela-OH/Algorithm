def solution(triangle):
    answer = 0
    dp = []
    for i in range(len(triangle)):
        dp.append([0 for _ in range(len(triangle[i]))])
    dp[0][0] = triangle[0][0]
    
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
            
    return max(dp[len(triangle) - 1])