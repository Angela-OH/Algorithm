import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True

    for e in edge[node]:
        if visited[e]:
            continue
        dfs(e)
        dp[node] += dp[e]

n, r, q = map(int, input().split())
edge = [[] for _ in range(n)]
dp = [1 for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)

dfs(r - 1)

for i in range(q):
    u = int(input())
    print(dp[u - 1])