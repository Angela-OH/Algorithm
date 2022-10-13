import sys

def min_max(maps, n):
    min = 101
    max = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] < min:
                min = maps[i][j]
            if maps[i][j] > max:
                max = maps[i][j]
    return (min, max)

def choose(n, maps, visited, height):
    index = ()
    for i in range(n):
        for j in range(n):
            if maps[i][j] > height and visited[i][j] == 0:
                return (i, j)
    return index

def dfs(n, maps, min_max):
    stack = []
    move = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]
    min = min_max[0] - 1
    max = min_max[1]
    space_max = 0

    for height in range(min, max):
        cnt = 0
        visited = [[0 for i in range(n)] for j in range(n)]
        while True:
            index = choose(n, maps, visited, height)
            if not index:
                break
            stack.append(index)
            visited[index[0]][index[1]] = 1
            cnt += 1

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
        if cnt > space_max:
            space_max = cnt

    return space_max

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    print(dfs(n, maps, min_max(maps, n)))