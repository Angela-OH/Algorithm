import sys
sys.setrecursionlimit(10 ** 6)
INF = sys.maxsize

answer = INF
di, dj = [0, -1, 1, 0], [-1, 0, 0, 1]
v = [False, True, True, False]

def dfs(board, dp, i, j, cost, isVertical):
    global answer
    if i == len(board) - 1 and j == len(board[0]) - 1:
        if cost < answer:
            answer = cost
        return
    if cost > answer or cost > (dp[i][j] + 400):
        return
    for k in range(4):
        if i == 0 and j == 0:
            isVertical = v[k]
        new_i, new_j = i + di[k], j + dj[k]
        if (0 <= new_i < len(board)) and (0 <= new_j < len(board[0])):
            if board[new_i][new_j] == 0:
                if (isVertical and v[k]) or (not isVertical and not v[k]):
                    new_cost = 100
                    new_isVertical = isVertical
                else:
                    new_cost = 600
                    new_isVertical = not(isVertical)
                board[i][j] = 1
                dp[new_i][new_j] = min(dp[new_i][new_j], dp[i][j] + new_cost)
                dfs(board, dp, new_i, new_j, cost + new_cost, new_isVertical)
                board[i][j] = 0
    return

def solution(board):
    dp = [[INF for _ in range(len(board[0]))] for _ in range(len(board))]
    dp[0][0] = 0
    dfs(board, dp, 0, 0, 0, False)
    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))