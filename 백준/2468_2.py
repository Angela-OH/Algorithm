import sys

def dfs(n, maps, i, j, height):
    stack = [(i, j)]
    move = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]

    while stack:
        node = stack.pop()
        x, y = node[0], node[1]
        for i in range(len(move)):
            a = x + move[i][0]
            b = y + move[i][1]
            if (0 <= a < n) and (0 <= b < n):
                if (maps[a][b] > height) and (visited[a][b] == 0):
                    stack.append((a, b))
                    visited[a][b] = 1


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    h_min = min(map(min, maps)) - 1
    h_max = max(map(max, maps))

    space_max = 0

    for height in range(h_min, h_max):
        cnt = 0
        visited = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if maps[i][j] > height and visited[i][j] == 0:
                    dfs(n, maps, i, j, height)
                    cnt += 1
        if cnt > space_max:
            space_max = cnt
    
    print(space_max)
