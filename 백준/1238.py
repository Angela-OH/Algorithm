import sys, heapq

def dijkstra(start, dest):
    heap = []
    heapq.heappush(heap, [0, start])
    time = [max for _ in range(n)]
    time[start] = 0

    while heap:
        now_time, now_start = heapq.heappop(heap)
        for a in arr[now_start]:
            t, end = a[0], a[1]
            new_time = now_time + t
            if time[end] > new_time:
                time[end] = new_time
                heapq.heappush(heap, [new_time, end])

    return time[dest]


n, m, x = map(int, input().split())
arr = [[] for _ in range(m)]
max = sys.maxsize
result = 0

for i in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    arr[a - 1].append((t, b - 1))

for i in range(n):
    if i == (x - 1):
        continue
    time = dijkstra(i, x - 1) + dijkstra(x - 1, i)
    if time > result:
        result = time

print(result)