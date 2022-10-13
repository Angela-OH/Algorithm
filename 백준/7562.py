import sys

def bfs(l, x1, y1, x2, y2):
    queue = [(x1, y1)]
    level = [[0 for i in range(l)] for j in range(l)]
    move = [
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1)
    ]
    
    while queue:
        node = queue.pop(0)
        x, y = node[0], node[1]
        if x == x2 and y == y2:
            return level[x][y]

        i = 0
        for i in range(8):
            a = x + move[i][0]
            b = y + move[i][1]
            if (0 <= a < l) and (0 <= b < l):
                if level[a][b] == 0:
                    level[a][b] = level[x][y] + 1
                    if x == x2 and y == y2:
                        return level[x][y]
                    queue.append((a, b))  

if __name__ == "__main__":
    c = int(sys.stdin.readline().rstrip())
    
    i = 0
    for i in range(c):
        l = int(sys.stdin.readline().rstrip())
        x1, y1 = map(int, sys.stdin.readline().rstrip().split())
        x2, y2 = map(int, sys.stdin.readline().rstrip().split())

        print(bfs(l, x1, y1, x2, y2))