def bfs(n, a, b, connect):
    visited = [0 for i in range(n + 1)]
    queue = [a]
    result = -1 

    while queue:
        node = queue.pop(0)
        for i in connect[node]:
            if visited[i] == 0: # not visited yet
                visited[i] = visited[node] + 1
                queue.append(i)
                if i == b:
                    result = visited[i]
                    return result

    return result

if __name__ == "__main__":
    n = int(input())
    connect = [[] for i in range(n + 1)]
    a, b = map(int, input().split())
    m = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        connect[x].append(y)
        connect[y].append(x)
    
    print(bfs(n, a, b, connect))