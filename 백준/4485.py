import sys, heapq
INF = sys.maxsize

def dijkstra(start, end):
    time = [INF for _ in range(n * n)]
    time[start] = arr[0][0]
    heap = []
    heapq.heappush(heap, [arr[0][0], start])

    while heap:
        now_time, now_start = heapq.heappop(heap)
        for c in connect[now_start]:
            new_time, new_start = c[0] + now_time, c[1]
            if time[new_start] > new_time:
                time[new_start] = new_time
                heapq.heappush(heap, [new_time, new_start])

    return time[end]

index = 0
while True:
    n = int(input())
    if n == 0:
        break
    index += 1
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    connect = [[] for _ in range(n * n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(n):  
            for dx, dy in d:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    connect[n * i + j].append((arr[x][y], x * n + y))

    print("Problem {}: {}".format(index, dijkstra(0, n * n - 1)))

        