import sys
from collections import deque

def bfs(m, n, box):
    queue = deque([])
    move = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1)
    ]
    zero_count = 0
    max = 0

    for a in range(n):
        for b in range(m):
            if box[a][b] == 0:
                zero_count += 1
            if box[a][b] == 1:
                queue.append((a, b))
    
    if zero_count == 0:
        return 0
    
    while queue:
        node = queue.popleft()
        y, x = node[0], node[1]
        for dx, dy in move:
            x1, y1 = x + dx, y + dy
            if (0 <= x1 < m) and (0 <= y1 < n):
                if box[y1][x1] == 0:
                    box[y1][x1] = box[y][x] + 1
                    if box[y1][x1] > max:
                        max = box[y1][x1]
                    zero_count -= 1
                    queue.append((y1, x1))      

    if zero_count != 0:
        return -1

    return max - 1
    
if __name__ == "__main__":
    m, n = map(int, input().split())
    box = [list(map(int, sys.stdin.readline().split())) for j in range(n)]
    
    print(bfs(m, n, box))