def bad_sequence(level):
    for i in range(level, 0, -1):
        length = level - i + 1
        if length >= i:
            break
        if ans[i:level + 1] == ans[i - length:i]:
            return 1
    return 0

def back_tracking(n, level, index):
    global ans
    global cnt

    if cnt != 0:
        return

    ans[level] = index
    if bad_sequence(level):
        return

    if level >= n:
        cnt += 1
        for i in range(1, n + 1):
            print(ans[i], end='')
        return

    for i in range(1, 4):
        back_tracking(n, level + 1, i)
    
n = int(input())
ans = [0 for i in range(n + 2)]
cnt = 0

back_tracking(n, 0, 0)