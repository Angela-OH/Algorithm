import heapq

def cal(a, b):
    x = abs(loc[a][0] - loc[b][0])
    y = abs(loc[a][1] - loc[b][1])
    return (x ** 2 + y ** 2) ** (1/2)

def prim(start):
    sum, edge = 0, 0
    heap = []
    heapq.heappush(heap, (0, start))
    visited = [0 for _ in range(n)]

    while heap:
        i, j = heapq.heappop(heap)
        if visited[j] != 0:
            continue
        visited[j] = 1
        sum += i
        edge += 1
        if edge == n:
            break
        
        for k in range(n):
            if k == j:
                continue
            heapq.heappush(heap, (arr[j][k], k))
            
    return sum

n = int(input())
loc = [[] for _ in range(n)]
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    loc[i] = list(map(float, input().split()))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x, y = loc[i], loc[j]
        arr[i][j] = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1/2)
    
print(prim(0))