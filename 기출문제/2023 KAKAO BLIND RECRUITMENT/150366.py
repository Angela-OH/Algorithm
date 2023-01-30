def solution(commands):
    answer = []
    board = [["EMPTY" for _ in range(51)] for _ in range(51)]
    group = [[0 for _ in range(51)] for _ in range(51)]
    group_cnt = 0
    for command in commands:
        command = command.split()
        if (command[0] == "UPDATE" and len(command) == 4):
            r, c, val = int(command[1]), int(command[2]), command[3]
            if group[r][c] == 0: # 그룹이 아직 없음
                board[r][c] = val
                continue
            for i in range(1, 51):
                for j in range(1, 51):
                    if group[i][j] == group[r][c]:
                        board[i][j] = val
        elif (command[0] == "UPDATE" and len(command) == 3):
            v1, v2 = command[1], command[2]
            for i in range(1, 51):
                for j in range(1, 51):
                    if board[i][j] == v1:
                        board[i][j] = v2
        elif (command[0] == "MERGE"):
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            # 같은 셀이면 무시
            if r1 == r2 and c1 == c2:
                continue
            if group[r1][c1] == group[r2][c2] and group[r1][c1] != 0:
                continue
            
            val = "EMPTY"
            # 병합 셀에 들어갈 값 정하기
            if (board[r1][c1] != "EMPTY"):
                val = board[r1][c1]
            elif (board[r2][c2] != "EMPTY"):
                val = board[r2][c2]
            
            # 그룹 짓기
            if group[r1][c1] == 0 and group[r2][c2] == 0: # 둘 다 그룹 없음
                group_cnt += 1
                group[r1][c1] = group_cnt
                group[r2][c2] = group_cnt
                board[r1][c1] = val
                board[r2][c2] = val
            elif group[r1][c1] == 0: # r2, c2만 그룹 있음
                group[r1][c1] = group[r2][c2]
                board[r1][c1] = val
                for i in range(1, 51):
                    for j in range(1, 51):
                        if group[i][j] == group[r2][c2]:
                            board[i][j] = val
            elif group[r2][c2] == 0: # r1, c1만 그룹 있음
                group[r2][c2] = group[r1][c1]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if group[i][j] == group[r1][c1]:
                            board[i][j] = val
                board[r2][c2] = val
            elif group[r1][c1] != group[r2][c2]: # 서로 다른 그룹
                grp = group[r2][c2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if group[i][j] == grp: # r2, c2 그룹 -> r1, c1 그룹에 통합
                            group[i][j] = group[r1][c1]
                        if group[i][j] == group[r1][c1]:
                            board[i][j] = val
        elif (command[0] == "UNMERGE"):
            r, c = int(command[1]), int(command[2])
            val = board[r][c]
            grp = group[r][c]
            if grp == 0: # unmerge 할 게 x
                continue
            for i in range(1, 51):
                for j in range(1, 51):
                    if group[i][j] == grp:
                        group[i][j] = 0
                        board[i][j] = "EMPTY"
            board[r][c] = val
        else:
            r, c = int(command[1]), int(command[2])
            answer.append(board[r][c])
    return answer