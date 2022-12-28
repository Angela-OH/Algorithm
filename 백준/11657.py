import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
edges = []
dp = [INF for _ in range(n)]
dp[0] = 0
isCycle = False

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))

for i in range(n):
    for a, b, c in edges:
        if dp[a] != INF and dp[a] + c < dp[b]:
            if i == n - 1:
                isCycle = True
            else:
                dp[b] = dp[a] + c

if isCycle:
    print(-1)
else:
    for i in range(1, n):
        if dp[i] == INF:
            print(-1)
        else:
            print(dp[i])