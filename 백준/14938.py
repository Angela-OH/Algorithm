import sys, heapq

def dijkstra(start):
    INF = sys.maxsize
    boundary = [INF for _ in range(n)]
    boundary[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        node_boundary, node_start = heapq.heappop(heap)

        for connect_start, connect_boundary in connect[node_start]:
            new_boundary = node_boundary + connect_boundary
            if new_boundary < boundary[connect_start]:
                boundary[connect_start] = new_boundary
                heapq.heappush(heap, (new_boundary, connect_start))
    
    sum = 0
    for i in range(n):
        if boundary[i] <= m:
            sum += item[i]
            
    return sum

n, m, r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))
connect = [[] for _ in range(n)]

for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    connect[a - 1].append((b - 1, l))
    connect[b - 1].append((a - 1, l))

max = 0
for i in range(n):
    result = dijkstra(i)
    if result > max:
        max = result

print(max)
