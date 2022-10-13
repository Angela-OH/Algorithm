import sys

r, c = map(int, sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().strip()) for i in range(r)]
max_count = 1

def bfs():
    global max_count
    queue = set([(0, 0, board[0][0])])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, route = queue.pop()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if (0 <= a < r) and (0 <= b < c) and board[a][b] not in route:
                    queue.add((a, b, route + board[a][b]))
                    max_count = max(max_count, len(route) + 1)

bfs()
print(max_count)