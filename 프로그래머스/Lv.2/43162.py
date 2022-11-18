def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    stack = []
    
    while True:
        node = -1
        for i in range(len(visited)):
            if visited[i] == 0:
                node = i
        if node == -1:
            break
        stack.append(node)
        visited[node] = 1
        answer += 1
        
        while stack:
            node = stack.pop()
            for i in range(n):
                if i == node:
                    continue
                if computers[node][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
            
    return answer