from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    visited[0] = 1 # 1번 노드
    queue = deque([])
    queue.append((0, 0))
    max_level = 0
    
    for e in edge:
        e = [i - 1 for i in e]
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    while queue:
        node, level = queue.popleft()
        if level > max_level:
            max_level = level
            answer = 1
        elif level == max_level:
            answer += 1
        for i in graph[node]:
            if visited[i] == 0:
                queue.append((i, level + 1))
                visited[i] = 1
    return answer