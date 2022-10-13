def bfs(comp):
    visited = [1]
    queue = [1]
    
    while queue:
        node = queue.pop(0) # BFS uses Queue
        for i in comp[node - 1]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return len(visited)-1

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    comp = [[] for i in range(n)]

    i = 0
    for i in range(m):
        l1, l2 = map(int, input().split())
        comp[l1-1].append(l2)
        comp[l2-1].append(l1)
    
    print(bfs(comp))
