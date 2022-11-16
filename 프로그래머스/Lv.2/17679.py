def delete_board(board, board_status, m, n):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board_status[i][j] == 1: # 지워야함
                board[i][j] = 0
                cnt += 1
    if cnt == 0:
        return (0, [])

    for i in range(n):
        for j in range(m):
            if board[j][i] == 0: # 내려줘야함
                for k in range(j, 0, -1):
                    board[k][i] = board[k - 1][i]
                board[0][i] = 0
    return (cnt, board)
def solution(m, n, board):
    answer = 0
    board = [[board[i][j] for j in range(len(board[i]))] for i in range(len(board))]
    di, dj = [1, 1, 0], [0, 1, 1]
    while True:
        board_status = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                now = board[i][j]
                if now == 0:
                    continue
                cnt = 0
                for k in range(3):
                    new_i, new_j = i + di[k], j + dj[k]
                    if 0 <= new_i < m and 0 <= new_j < n:
                        if board[new_i][new_j] == now:
                            cnt += 1
                    if cnt == 3: # 지울 수 있음
                        board_status[i][j] = 1
                        for k in range(3):
                            new_i, new_j = i + di[k], j + dj[k]
                            board_status[new_i][new_j] = 1
        cnt, board = delete_board(board, board_status, m, n)
        if cnt == 0:
            break
        answer += cnt
    return answer