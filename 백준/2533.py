import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    
    for e in edge[node]:
        if visited[e]:
            continue
        dfs(e)
        dp[node][0] += dp[e][1] # node를 선택 x
        dp[node][1] += min(dp[e][0], dp[e][1]) # node를 선택 o

n = int(input())
edge = [[] for _ in range(n)]
dp = [[0, 1] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)

dfs(0)

print(min(dp[0][0], dp[0][1]))