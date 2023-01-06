import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    
    for e in edge[node]:
        if visited[e]:
            continue
        dfs(e)
        dp[node][0] += max(dp[e][0], dp[e][1]) # 해당 트리를 선택 x
        dp[node][1] += dp[e][0] # 해당 트리를 선택 o (자식 노드는 선택되면 안됨)

n = int(input())
population = list(map(int, input().split()))
edge = [[] for _ in range(n)]
dp = [[0, p] for p in population]
visited = [False for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

dfs(0)

print(max(dp[0][0], dp[0][1]))

