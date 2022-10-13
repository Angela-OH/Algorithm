import sys

def choose(graph, visited, index):
    for index in range(len(graph)):
        if (index + 1) not in visited:
            return index
    return index

def dfs(n, graph):
    visited = list()
    stack = list()
    count = 0

    start = choose(graph, visited, 0)

    while len(visited) != n:
        visited.append(start + 1)
        stack.append(start + 1)
        while stack:
            node = stack.pop()
            for i in graph[node - 1]:
                if i not in visited:
                    visited.append(i)
                    stack.append(i)
        count += 1
        start = choose(graph, visited, start)
    
    return count


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for i in range(n)]

    i = 0
    for i in range(m):
        input1, input2 = map(int, sys.stdin.readline().rstrip().split())
        graph[input1-1].append(input2)
        graph[input2-1].append(input1)

    print(dfs(n, graph))