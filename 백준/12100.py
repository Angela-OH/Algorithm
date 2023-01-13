import sys
input = sys.stdin.readline

def rotate(board2, degree): 
    if degree == 1: # 시계 방향으로 90도 회전
        return [[b[i] for b in board2[::-1]] for i in range(n)]
    elif degree == 2: # 반시계 방향으로 90도 회전
        return [[b[i] for b in board2[::]] for i in range(n - 1, -1, -1)]
    else: # 반전
        return [b[::-1] for b in board2[::]]

def slide(board2, dir):
    if dir == 2: # 오른쪽으로 밀기
        board2 = rotate(board2, 3) # 반전
    elif dir == 3: # 위로 밀기
        board2 = rotate(board2, 2) # 반시계 방향으로 90도 회전
    elif dir == 4: # 아래로 밀기
        board2 = rotate(board2, 1) # 시계 방향으로 90도 회전

    for i in range(n):
        # 왼쪽으로 밀기
        new_board = []
        for j in range(n):
            if board2[i][j] != 0: # 빈칸이 아니면 
                new_board.append(board2[i][j]) # 밀어야 할 대상

        # 합치기
        board2[i] = []
        idx = 0
        while idx < len(new_board):
            if idx == len(new_board) - 1:
                board2[i].append(new_board[idx])
                idx += 1
                continue

            if new_board[idx] == new_board[idx + 1]:
                board2[i].append(new_board[idx] * 2)
                idx += 2
            else:
                board2[i].append(new_board[idx])
                idx += 1
                
        board2[i].extend([0 for _ in range(n - len(board2[i]))])

    if dir == 2: 
        board2 = rotate(board2, 3)
    elif dir == 3: 
        board2 = rotate(board2, 1) 
    elif dir == 4: 
        board2 = rotate(board2, 2) 

    return board2[::]

def play(board2, cnt):
    global answer

    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board2[i][j])
        return

    cnt += 1
    
    play(slide(board2[::], 1), cnt)
    play(slide(board2[::], 2), cnt)
    play(slide(board2[::], 3), cnt)
    play(slide(board2[::], 4), cnt)

n = int(input())
answer = 0

def main():
    board = [list(map(int, input().split())) for _ in range(n)]

    play(board[::], 0)

    print(answer)

main()