import sys
input = sys.stdin.readline

def move(d, s):
    new_cloud = []
    for x, y in cloud:
        visited[x][y] = False

    for x, y in cloud:
        new_x, new_y = x + gap[d][0] * s, y + gap[d][1] * s
        new_cloud.append((new_x % n, new_y % n))
        visited[new_x % n][new_y % n] = True
    return new_cloud

def water():
    for x, y in cloud:
        board[x][y] += 1

def copy():
    for x, y in cloud:
        count = 0
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n:
                if board[new_x][new_y] != 0:
                    count += 1
        board[x][y] += count

def create():
    new_cloud = []

    for i in range(n):
        for j in range(n):
            if (board[i][j] >= 2) and (not visited[i][j]):
                visited[i][j] = True
                new_cloud.append((i, j))
                board[i][j] -= 2

    for x, y in cloud:
        visited[x][y] = False

    return new_cloud

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
gap = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
visited = [[False for _ in range(n)] for _ in range(n)]
answer = 0

for i in range(m):
    d, s = map(int, input().split())
    cloud = move(d - 1, s) # 1번
    water() # 2번
    copy() # 4번
    cloud = create() # 5번

for i in range(n):
    for j in range(n):
        answer += board[i][j]

print(answer)