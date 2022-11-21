from collections import deque
def changable(before, after):
    length = len(before)
    cnt = 0
    for i in range(length):
        if before[i] != after[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
    
def bfs(begin, target, words):
    queue = deque([])
    queue.append((begin, 0))
    visited = [0 for _ in range(len(words))]
    
    while queue:
        node, level = queue.popleft()
        if node == target:
            return level
        for i, word in enumerate(words):
            if changable(node, word) and visited[i] == 0:
                queue.append((word, level + 1))
                visited[i] = 1
    return 0 # target으로 변환 불가

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    return bfs(begin, target, words)