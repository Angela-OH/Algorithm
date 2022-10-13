import sys

def dfs(graph, start, visited):
    visited.append(start)
    print("{} ".format(start), end = "")

    for i in graph[start - 1]:
        if i not in visited:
            dfs(graph, i, visited)

def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        print("{} ".format(node), end = "")
        for i in graph[node - 1]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

if __name__ == "__main__":
    n, m, start = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for index in range(n)]

    i = 0
    for i in range(m):
        l1, l2 = map(int, sys.stdin.readline().rstrip().split())
        graph[l1-1].append(l2)
        graph[l2-1].append(l1)

    i = 0
    for i in range(n):
        graph[i].sort()

    visited = []
    dfs(graph, start, visited)
    print()
    bfs(graph, start)