import sys
input = sys.stdin.readline

n = int(input())
drink = [int(input()) for _ in range(n)]
dp = [[] for _ in range(n + 2)]
dp[0], dp[1] = [0, 0], [0, 0]
if drink[0] != 0:
    dp[2] = [drink[0], 1]
else:
    dp[2] = [0, 0]

for i in range(3, n + 2):
    if drink[i - 2] == 0: # 선택할 필요 x
        dp[i] = [dp[i - 1][0], 0]
        continue
    if dp[i - 1][1] < 2: # 이어서 추가 가능
        dp[i] = [dp[i - 1][0] + drink[i - 2], dp[i - 1][1] + 1]
    else: # 포도주는 연속 3개 선택 불가
        compare = max(dp[i - 1][0], dp[i - 2][0] + drink[i - 2], dp[i - 3][0] + drink[i - 3] + drink[i - 2])
        
        if compare == dp[i - 1][0]: # 이전까지의 해가 최적해
            dp[i] = [dp[i - 1][0], 0]
        elif compare == (dp[i - 2][0] + drink[i - 2]): # 현재 - 2까지의 최대 포도주와 현재 포도주 선택
            dp[i] = [dp[i - 2][0] + drink[i - 2], 1]
        else: # 현재 포도주 + 이전 포도주를 선택하는게 더 이득
            dp[i] = [dp[i - 3][0] + drink[i - 3] + drink[i - 2], 2]

max = 0
for i in range(2, n + 2):
    if dp[i][0] > max:
        max = dp[i][0]
print(max)