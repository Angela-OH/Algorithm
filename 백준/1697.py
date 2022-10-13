import sys
from collections import deque

def bfs(n, k):

    if n == k:
        return 0

    visited = [0 for i in range(100001)]
    visited[n] = 1
    queue = deque([(n, 0)])
    
    while queue:
        node = queue.popleft()
        move = [node[0] + 1, node[0] - 1, node[0] * 2]
        level = node[1] + 1
        for i in move:
            if i == k:
                return level
            if 0 < i <= 100000:
                if visited[i] == 0:
                    queue.append((i, level))
                    visited[i] = 1

if __name__ == "__main__":
    n, k = map(int, input().split())

    print(bfs(n, k))