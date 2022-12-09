from collections import deque

def node_count(n, network, w):
    queue = deque([])
    queue.append(w)
    visited = [0 for _ in range(n)]
    visited[w] = 1
    count = 1
    
    while queue:
        node = queue.popleft()
        for i in range(n):
            if network[node][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                count += 1
    return count

def solution(n, wires):
    answer = 101
    network = [[0 for _ in range(n)] for _ in range(n)]
    for w1, w2 in wires:
        network[w1 - 1][w2 - 1] = 1
        network[w2 - 1][w1 - 1] = 1
    
    for w1, w2 in wires:
        network[w1 - 1][w2 - 1] = 0
        network[w2 - 1][w1 - 1] = 0
        result = abs(node_count(n, network, w1 - 1) - node_count(n, network, w2 - 1))
        if result < answer:
            answer = result
        network[w1 - 1][w2 - 1] = 1
        network[w2 - 1][w1 - 1] = 1
        
    return answer