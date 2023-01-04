import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v)]
dp = [INF for _ in range(v)]
dp[k - 1] = 0
edge = []

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append((c, b - 1))

heapq.heappush(edge, (0, k - 1))
while edge:
    dis, node = heapq.heappop(edge)
    if dp[node] < dis:
        continue
    for next_dis, next_node in graph[node]:
        if dis + next_dis < dp[next_node]:
            heapq.heappush(edge, (dis + next_dis, next_node))
            dp[next_node] = dis + next_dis

for i in range(v):
    if dp[i] == INF:
        print('INF')
    else:
        print(dp[i])