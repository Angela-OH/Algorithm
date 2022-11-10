from collections import deque

def count(g, node):
    child = [1 for _ in range(node)]
    ans = []
    queue = deque([])
    queue.append((0, -1))
    visited = [0 for _ in range(node)]
    visited[0] = 1

    while queue:
        result, before = queue.popleft()
        ans.append((result, before))
        for i in range(node):
            if g[result][i] == 1 and visited[i] == 0:
                queue.append((i, result))
                visited[i] = 1
    
    for i in range(len(ans) - 1, 0, -1):
        now, before = ans[i]
        child[before] += child[now]
    
    return child

def solution(edges):
    node = len(edges) + 1
    g = [[0 for _ in range(node)] for _ in range(node)]
    max = 0

    for i in range(len(edges)):
        for j in range(len(edges[0])):
            edges[i][j] = int(edges[i][j])

    for e1, e2 in edges:
        g[e1][e2] = 1
        g[e2][e1] = 1
    
    child = count(g, node)

    for e1, e2 in edges:
        if child[e1] > child[e2]:
            value = (node - child[e2]) * child[e2] * 2
        else:
            value = (node - child[e1]) * child[e1] * 2
        if value > max:
            max = value

    return max

'''
ex1 = [[0, 2], [1, 2], [3, 1]] 
ex2 = [[0, 1], [1, 2], [1, 3], [3, 4]]
ex3 = [[0, 1], [1, 2], [1, 3], [3, 4], [0, 5]] #16
ex4 = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5]] #18
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
print(solution(ex4))
'''
