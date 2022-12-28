import sys
input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())
dp = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for i in range(k):
    a, b = map(int, input().split())
    dp[a - 1][b - 1] = 1

for i in range(n): # 거쳐가는 노드
    for j in range(n): # 시작 노드
        for u in range(n): # 도착 노드
            dp[j][u] = min(dp[j][u], dp[j][i] + dp[i][u])

s = int(input())
for i in range(s):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if dp[a][b] == dp[b][a]:
        print(0)
    elif dp[a][b] < dp[b][a]:
        print(-1)
    else:
        print(1)