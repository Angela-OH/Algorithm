def solution(board):
    answer = 0
    row, column = len(board), len(board[0])
    new_board = [[0 for _ in range(column + 1)]]
    dp = [[0 for _ in range(column)] for _ in range(row)]
    for b in board:
        new_board.append([0] + b)

    for i in range(row):
        for j in range(column):
            if new_board[i+1][j+1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            if dp[i][j] > answer:
                answer = dp[i][j]
                
    return answer ** 2