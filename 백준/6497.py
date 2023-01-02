import sys, heapq
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    con = [[] for _ in range(m)]
    visited = set()
    total = 0
    save = 0

    if m == 0 and n == 0:
        break

    for i in range(n):
        x, y, z = map(int, input().split())
        total += z
        con[x].append((z, y))
        con[y].append((z, x))

    visited.add(0)
    edges = con[0]
    heapq.heapify(edges)

    for i in range(m - 1):
        dis, node = heapq.heappop(edges)
        while node in visited:
            dis, node = heapq.heappop(edges)
        visited.add(node)
        save += dis
        for c in con[node]:
            if c[1] not in visited:
                heapq.heappush(edges, c)
    
    print(total - save)
    