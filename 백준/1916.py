import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    dp[start - 1] = 0
    heapq.heappush(heap, (0, start - 1))

    while heap:
        dis, node = heapq.heappop(heap)
    
        if dp[node] < dis: # 더 이상 탐색할 필요 x
            continue

        for next_dis, next_node in edge[node]:
            if dis + next_dis < dp[next_node]:
                dp[next_node] = dis + next_dis
                heapq.heappush(heap, (dis + next_dis, next_node))

n = int(input())
m = int(input())

edge = [[] for _ in range(n)]
dp = [INF for _ in range(n)]
heap = []

for i in range(m):
    a, b, c = map(int, input().split())
    edge[a - 1].append((c, b - 1))
start, end = map(int, input().split())

dijkstra()

print(dp[end - 1])