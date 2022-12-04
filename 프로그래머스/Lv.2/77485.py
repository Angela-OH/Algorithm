def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = columns * i + j + 1
            
    for query in queries:
        query = [i - 1 for i in query]
        topLeft = board[query[0]][query[1]]
        bottomRight = board[query[2]][query[3]]
        num = set([topLeft, bottomRight])
        
        for i in range(query[0], query[2]):
            board_num = board[i + 1][query[1]]
            board[i][query[1]] = board_num
            num.add(board_num)
        
        for i in range(query[2], query[0], -1):
            board_num = board[i - 1][query[3]]
            board[i][query[3]] = board_num
            num.add(board_num)
        
        for j in range(query[3], query[1] + 1, -1):
            board_num = board[query[0]][j - 1]
            board[query[0]][j] = board_num
            num.add(board_num)
        
        for j in range(query[1], query[3]):
            board_num = board[query[2]][j + 1]
            board[query[2]][j] = board_num
            num.add(board_num)
            
        board[query[0]][query[1] + 1] = topLeft
        board[query[2]][query[3] - 1] = bottomRight
        
        answer.append(min(num))
        
    return answer