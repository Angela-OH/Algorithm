import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):

    if visited[x][y]:
        print(-1)
        exit()

    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1
    val = int(board[x][y])

    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + i * val, y + j * val
        if (0 <= new_x < n) and (0 <= new_y < m):
            if board[new_x][new_y] != 'H':
                visited[x][y] = True
                dp[x][y] = max(dp[x][y], dfs(new_x, new_y) + 1)
                visited[x][y] = False
    
    return dp[x][y]

n, m = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)] # 값 재사용을 위해
visited = [[False for _ in range(m)] for _ in range(n)] # 현재 탐색 중인 루트에서 이미 방문한 적이 있는지?

dfs(0, 0)

print(dp[0][0])