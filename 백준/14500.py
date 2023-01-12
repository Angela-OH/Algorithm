import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

answer = 0

def dfs(i, j, cnt, sum):
    global answer

    if cnt == 4:
        answer = max(answer, sum)
        return

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < n and 0 <= new_j < m:
            if not visited[new_i][new_j]:
                visited[new_i][new_j] = True
                dfs(new_i, new_j, cnt + 1, sum + board[new_i][new_j])
                visited[new_i][new_j] = False

def check(i, j):
    global answer

    tetro = [
        [(0, 0), (0, 1), (0, 2), (1, 1)], 
        [(0, 0), (1, 0), (1, 1), (2, 0)],
        [(0, 0), (1, -1), (1, 0), (2, 0)],
        [(0, 0), (1, -1), (1, 0), (1, 1)]
    ]

    for t in tetro:
        sum = 0
        for di, dj in t:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < n and 0 <= new_j < m:
                sum += board[new_i][new_j]
            else:
                sum = 0
                break
        answer = max(answer, sum)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check(i, j) # 마지막 테트로미노는 dfs로 계산 불가

print(answer)