import sys, heapq

def dijkstra():
    INF = sys.maxsize
    cost = [INF for _ in range(m * n)]
    cost[0] = 0
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    heap = []
    heapq.heappush(heap, [0, 0])

    while heap:
        count, index = heapq.heappop(heap)
        for dx, dy in d:
            x, y = index // m, index % m
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m:
                new_index = new_x * m + new_y
                new_count = count + arr[new_x][new_y]
                if cost[new_index] > new_count:
                    cost[new_index] = new_count
                    heapq.heappush(heap, [new_count, new_index])

    return cost[m * n - 1]

m, n = map(int, input().split())
arr = [[] for _ in range(n)]
maze = [0 for _ in range(m * n)]

for i in range(n):
    input_text = sys.stdin.readline().strip()
    for text in input_text:
        arr[i].append(int(text))

# Dijkstra Algorithm
print(dijkstra())