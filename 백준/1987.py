max = 0

def dfs(r, c, board, index, visited):
    move = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    x, y, level = index[0], index[1], index[2]
    for dx, dy in move:
        a, b = x + dx, y + dy
        if (0 <= a < r) and (0 <= b < c):
            if visited[ord(board[a][b])-65] == 0:
                visited[ord(board[a][b])-65] = 1
                dfs(r, c, board, (a, b, level + 1), visited)
                visited[ord(board[a][b])-65] = 0

    global max
    if level > max:
        max = level

if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [[0 for i in range(c)] for j in range(r)]

    for i in range(r):
        text = input()
        for j in range(c):
            board[i][j] = text[j]
    
    visited = [0 for i in range(26)]
    visited[ord(board[0][0])-65] = 1
    
    dfs(r, c, board, (0, 0, 1), visited)

    print(max)