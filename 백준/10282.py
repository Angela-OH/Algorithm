import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

t = int(input())
for i in range(t):
    n, d, c = map(int, input().split())
    con = [[] for _ in range(n)]
    dp = [INF for _ in range(n)]
    dp[c - 1] = 0
    heap = []
    answer = 0
    max = 0

    for j in range(d):
        a, b, s = map(int, input().split())
        con[b - 1].append((a - 1, s))

    heapq.heappush(heap, (0, c - 1))
    while heap:
        dis, node = heapq.heappop(heap)
        if dp[node] < dis: # 어차피 최소 가중치가 아님
            continue
        for next_node, next_dis in con[node]:
            val = next_dis + dis
            if val < dp[next_node]:
                dp[next_node] = val
                heapq.heappush(heap, (val, next_node))

    for d in dp:
        if d != INF:
            answer += 1
            if d > max:
                max = d
                
    print("{} {}".format(answer, max))