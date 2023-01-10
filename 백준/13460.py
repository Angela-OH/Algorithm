from collections import deque
import copy

def count(board, ball, direction, start, end, rng):
    cnt = 0
    if direction == 1 or direction == 2:
        for i in range(start, end, rng):
            if board[ball[0]][i] == '.':
                cnt += 1
            elif board[ball[0]][i] == '#':
                break
            elif board[ball[0]][i] == 'O':
                cnt = -1
                break
    else:
        for i in range(start, end, rng):
                if board[i][ball[1]] == '.':
                    cnt += 1
                elif board[i][ball[1]] == '#':
                    break
                elif board[i][ball[1]] == 'O':
                    cnt = -1
                    break
    return cnt

def tilt(board, direction, ball):

    if direction == 1: # 좌
        start, end, range = ball[1] - 1, -1, -1
    elif direction == 2: # 우
        start, end, range = ball[1] + 1, m, 1
    elif direction == 3: # 위
        start, end, range = ball[0] - 1, -1, -1
    else: # 아래
        start, end, range = ball[0] + 1, n, 1

    cnt = count(board, ball, direction, start, end, range)
    if cnt == -1:
        return cnt
    
    if direction == 1: # 좌
        return (ball[0], ball[1] - cnt)
    elif direction == 2: # 우
        return (ball[0], ball[1] + cnt)
    elif direction == 3: # 위
        return (ball[0] - cnt, ball[1])
    else: # 아래
        return (ball[0] + cnt, ball[1])

def move(board, blue, red):
    direction = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    queue = deque([])
    queue.append((board, blue, red, -1, 0))
    cnt = 0

    while queue and cnt <= 10:
        board, blue, red, dir, cnt = queue.popleft()
        cnt += 1
        for d in [1, 2, 3, 4]:
            if d == dir:
                continue
            if board[blue[0] + direction[d][0]][blue[1] + direction[d][1]] == '#':
                if board[red[0] + direction[d][0]][red[1] + direction[d][1]] == '#':
                    continue
            new_blue = tilt(board, d, blue)
            new_red = tilt(board, d, red)
            if new_blue == -1:
                continue
            elif new_red == -1:
                return cnt
            else:
                new_board = copy.deepcopy(board)
                new_board[blue[0]][blue[1]] = '.'
                new_board[new_blue[0]][new_blue[1]] = 'B'
                new_board[red[0]][red[1]] = '.'
                new_board[new_red[0]][new_red[1]] = 'R'
                queue.append((new_board, new_blue, new_red, d, cnt))
    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'R':
            red = (i, j) 

print(move(board, blue, red))

