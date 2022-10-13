import sys

def dfs(n, pic):
    stack = []
    visited = [[0 for i in range(n)] for j in range(n)]
    move = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    num = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                stack.append((i, j, pic[i][j]))
                visited[i][j] = 1

                while stack:
                    node = stack.pop()
                    x, y, color = node[0], node[1], node[2]
                    for dx, dy in move:
                        a, b = x + dx, y + dy
                        if (0 <= a < n) and (0 <= b < n):
                            if pic[a][b] == color and visited[a][b] == 0:
                                visited[a][b] = 1
                                stack.append((a, b, pic[a][b]))

                num += 1

    return num

if __name__ == "__main__":
    n = int(input())
    pic = [[] for _ in range(n)]
    pic_2 = [[] for _ in range(n)]

    for i in range(n):
        text = sys.stdin.readline().strip()
        pic[i] = text
        pic_2[i] = text.replace("R", "G")

    print(dfs(n, pic), end = " ")
    print(dfs(n, pic_2))