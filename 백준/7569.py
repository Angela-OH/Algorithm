import sys
from collections import deque

def bfs(m, n, h, box):
    queue = deque([])
    move = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
    ]
    zero_count = 0
    max = 0

    for a in range(h):
        for b in range(n):
            for c in range(m):
                if box[a][b][c] == 0:
                    zero_count += 1
                if box[a][b][c] == 1:
                    queue.append((a, b, c))
    
    if zero_count == 0:
        return 0
    
    while queue:
        node = queue.popleft()
        z, y, x = node[0], node[1], node[2]
        for dx, dy, dz in move:
            x1, y1, z1 = x + dx, y + dy, z + dz
            if (0 <= x1 < m) and (0 <= y1 < n) and (0 <= z1 < h):
                if box[z1][y1][x1] == 0:
                    box[z1][y1][x1] = box[z][y][x] + 1
                    if box[z1][y1][x1] > max:
                        max = box[z1][y1][x1]
                    zero_count -= 1
                    queue.append((z1, y1, x1))      

    if zero_count != 0:
        return -1

    return max - 1
    
if __name__ == "__main__":
    m, n, h = map(int, input().split())
    box = [[list(map(int, sys.stdin.readline().split())) for j in range(n)] for u in range(h)]
    
    print(bfs(m, n, h, box))