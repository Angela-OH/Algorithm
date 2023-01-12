import sys
input = sys.stdin.readline

def slide(i, idx, val, isHorizontal):
    cnt = 1

    for j in range(idx + 1, idx + l):
        if j >= n:
            break
        elif isHorizontal and board[i][j] == val:
            cnt += 1
        elif (not isHorizontal) and board[j][i] == val:
            cnt += 1
        else:
            break

    if cnt != l:
        return False

    return True

def check(i, isHorizontal):
    global answer

    if isHorizontal:
        h = board[i][0]
    else:
        h = board[0][i]
    idx, stable = 1, 1

    while idx < n:
        if isHorizontal:
            val = board[i][idx]
        else:
            val = board[idx][i]

        if val == h:
            idx += 1
            stable += 1
        elif (val - h) == 1: # 높이가 높아짐
            if stable < l:
                break
            idx += 1
            h = val
            stable = 1
        elif (val - h) == -1: # 높이가 낮아짐
            if not slide(i, idx, val, isHorizontal):
                break
            h = val
            idx += l
            stable = 0
        else:
            break
    if idx == n:
        answer += 1         

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    check(i, True)
    check(i, False)

print(answer)