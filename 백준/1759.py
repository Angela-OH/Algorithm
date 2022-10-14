def back_tracking(l, c, str, level, index):
    global ans
    # 종료 조건
    if index >= c:
        return
    if (l - level) >= (c - index):
        return

    if index != -1:
        ans[level] = str[index]

    if level >= l:
        cnt = 0
        for i in ['a', 'e', 'i', 'o', 'u']:
            if i in ans:
                cnt += 1
        if cnt == 0:
            return
        if (l - cnt) < 2:
            return

        for i in range(1, l + 1):
            print(ans[i], end="")
        print()
        return
    for i in range(index + 1, c):
        back_tracking(l, c, str, level + 1, i)

l, c = map(int, input().split())
str = list(input().split())
str.sort()
ans = [0 for _ in range(l + 1)]

back_tracking(l, c, str, 0, -1)