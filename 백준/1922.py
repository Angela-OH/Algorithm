import sys, heapq
input = sys.stdin.readline

def prim(start):
    sum, count = 0, 0
    visited = [0 for _ in range(n)]

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        i, j = heapq.heappop(heap)
        if visited[j]:
            continue
        visited[j] = 1
        sum += i
        count += 1
        if count == n - 1:
            break
        for c in cost[j]:
            heapq.heappush(heap, c)

    return sum

n = int(input())
m = int(input())
cost = [[] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    cost[a - 1].append((c, b - 1))
    cost[b - 1].append((c, a - 1))

for i in range(len(cost)):
    if cost[i]:
        print(prim(i))
        break