import sys
from collections import deque

def bfs(forest, start_s, start_w, r, c):
    start_s.extend([0])
    queue_s, queue_w = deque([start_s]), deque(start_w)
    visited_s = [[0 for i in range(c)] for j in range(r)]
    visited_w = [[0 for i in range(c)] for j in range(r)]
    visited_s[start_s[0]][start_s[1]] = 1
    for w in start_w:
        visited_w[w[0]][w[1]] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue_w:
        x, y, time = queue_w.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if (0 <= a < r) and (0 <= b < c) and visited_w[a][b] == 0:
                if forest[a][b] == 0:
                    forest[a][b] = time + 1
                    visited_w[a][b] = 1
                    queue_w.append([a, b, time + 1])

    while queue_s:
        x, y, time = queue_s.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if (0 <= a < r) and (0 <= b < c) and visited_s[a][b] == 0:
                if forest[a][b] == -4:
                    return (time + 1)
                if forest[a][b] == -2 or forest[a][b] == -1:
                    continue
                if forest[a][b] == 0 or (time + 1) < forest[a][b]:
                    visited_s[a][b] = 1
                    queue_s.append([a, b, time + 1])

    return "KAKTUS"

r, c = map(int, sys.stdin.readline().rstrip().split())
forest = [[0 for i in range(c)] for j in range(r)]
water = []
for i in range(r):
    text = sys.stdin.readline().strip()
    for j in range(len(text)):
        if text[j] == "X":
            forest[i][j] = -2
        elif text[j] == "*":
            water.append([i, j, 0])
            forest[i][j] = -1
        elif text[j] == "S":
            start = [i, j]
            forest[i][j] = -3
        elif text[j] == "D":
            forest[i][j] = -4

print(bfs(forest, start, water, r, c))