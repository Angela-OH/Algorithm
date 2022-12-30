import sys, math
input = sys.stdin.readline

# 0 - 1 knapsack
n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
bag = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1): # 배낭에 넣을 물건 번호
    for j in range(1, k + 1): # 현재 배낭 무게
        w, v = bag[i - 1][0], bag[i - 1][1]
        if j < w: # 현재 배낭 무게 < 배낭에 넣고자 하는 물건 무게 
            dp[i][j] = dp[i - 1][j] # 배낭에 못 넣음!
        else: # 현재 물건을 배낭에 넣을 수 있을 때
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v) # 지금까지의 최대 or 현재 물건을 배낭에 담았을 때

        
print(dp[n][k])