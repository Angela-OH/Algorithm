from collections import deque

def bfs(i, j):
    queue = deque([])
    queue.append((i, j))
    graph[i][j] = count
    visited[i][j] = True

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            new_i, new_j = i + dx[k], j + dy[k]
            if 0 <= new_i < n and 0 <= new_j < m:
                if graph[new_i][new_j] == 1 and not visited[new_i][new_j]:
                    graph[new_i][new_j] = count
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j))

def find(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
count = 1
answer = 0
node = 0

# 섬 분리하기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 or visited[i][j]:
            continue
        bfs(i, j)
        count += 1

# 다리 길이 구하기
edge = [[101 for _ in range(count - 1)] for _ in range(count - 1)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        start_node = graph[i][j]
        for k in range(i + 1, n):
            if graph[k][j] == start_node:
                break
            if graph[k][j] != 0:
                if k - i > 2:
                    end_node = graph[k][j]
                    edge[start_node - 1][end_node - 1] = min(edge[start_node - 1][end_node - 1], (k - i - 1))
                break
        for k in range(j + 1, m):
            if graph[i][k] == start_node:
                break
            if graph[i][k] != 0:
                if k - j > 2:
                    end_node = graph[i][k]
                    edge[start_node - 1][end_node - 1] = min(edge[start_node - 1][end_node - 1], (k - j - 1))
                break

# Kruskal
edges = []
parent = [-1 for _ in range(count - 1)]
for i in range(len(edge)):
    for j in range(len(edge)):
        if edge[i][j] != 101:
            edges.append((edge[i][j], i, j))
edges.sort()

for dis, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        answer += dis
        node += 1

if answer == 0 or node < count - 2:
    print(-1)
else:
    print(answer)