def solution(commands):
    answer = []
    board = [["EMPTY" for _ in range(51)] for _ in range(51)]
    group = [[(i, j) for j in range(51)] for i in range(51)]
    for command in commands:
        command = command.split()
        if (command[0] == "UPDATE" and len(command) == 4):
            x, y, val = int(command[1]), int(command[2]), command[3]
            r, c = group[x][y]
            board[r][c] = val
        elif (command[0] == "UPDATE" and len(command) == 3):
            v1, v2 = command[1], command[2]
            for i in range(1, 51):
                for j in range(1, 51):
                    if board[i][j] == v1:
                        board[i][j] = v2
        elif (command[0] == "MERGE"):
            x1, y1, x2, y2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            # 같은 셀이면 무시
            if group[x1][y1] == group[x2][y2]:
                continue
            
            r1, c1 = group[x1][y1]
            r2, c2 = group[x2][y2]
            
            # 병합 셀에 들어갈 값 정하기
            val = board[r1][c1]
            if (board[r1][c1] != "EMPTY"):
                val = board[r1][c1]
            elif (board[r2][c2] != "EMPTY"):
                val = board[r2][c2]
            board[r1][c1] = val
            
            # 그룹 짓기 (x2, y2를 x1, y1 그룹에 합류)
            for i in range(1, 51):
                for j in range(1, 51):
                    if group[i][j] == (r2, c2):
                        group[i][j] = group[x1][y1]
        elif (command[0] == "UNMERGE"):
            x, y = int(command[1]), int(command[2])
            r, c = group[x][y]
            val = board[r][c]
            board[r][c] = "EMPTY"
            
            for i in range(1, 51):
                for j in range(1, 51):
                    if group[i][j] == (r, c):
                        group[i][j] = (i, j)
                        board[i][j] = "EMPTY"
            board[x][y] = val
        else:
            x, y = int(command[1]), int(command[2])
            r, c = group[x][y]
            answer.append(board[r][c])
    return answer