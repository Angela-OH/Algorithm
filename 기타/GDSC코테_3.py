def cnt(node, other_node, g, l):
    stack = [node]
    visited = [0 for _ in range(l)]
    visited[node] = 1
    visited[other_node] = 1
    count = 0
    while stack:
        result = stack.pop()
        count += 1
        for i in range(l):
            if g[result][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1

    return count

def solution(edges):
    node = len(edges) + 1
    g = [[0 for _ in range(node)] for _ in range(node)]
    max = 0
    
    for e1, e2 in edges:
        g[e1][e2] = 1
        g[e2][e1] = 1
    
    for e1, e2 in edges:
        value = cnt(e1, e2, g, node) * cnt(e2, e1, g, node) * 2
        if value > max:
            max = value

    return max
    
ex1 = [[0, 2], [1, 2], [3, 1]] 
ex2 = [[0, 1], [1, 2], [1, 3], [3, 4]]
ex3 = [[0, 1], [1, 2], [1, 3], [3, 4], [0, 5]] #16
ex4 = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5]] #18
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
print(solution(ex4))
