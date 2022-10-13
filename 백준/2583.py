import sys

def check(m, n, square):
    index = ()
    for a in range(m):
        for b in range(n):
            if square[a][b] == 0:
                index = (a, b)
                return index
    return index

def dfs(m, n, square):
    stack = []
    move = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    ]
    space = []

    while True:
        index = check(m, n, square)
        if not index:
            break
        square[index[0]][index[1]] = -1
        stack.append(index)

        cnt = 1
        while stack:
            node = stack.pop()
            x, y = node[0], node[1]

            for i in range(len(move)):
                a = x + move[i][0]
                b = y + move[i][1]
                if (0 <= a < m) and (0 <= b < n):
                    if square[a][b] == 0:
                        stack.append((a, b))
                        square[a][b] = -1
                        cnt += 1
        space.append(cnt)

    return space

if __name__ == "__main__":
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    square = [[0 for i in range(n)] for j in range(m)]
    space = []

    for a in range(k):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        for b in range(y1, y2):
            for c in range(x1, x2):
                square[b][c] = 1

    space = dfs(m, n, square)
    space.sort()

    space_cnt = len(space)
    print(space_cnt)

    i = 0
    for i in range(space_cnt):
        print(space[i], end=" ")

    