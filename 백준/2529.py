def back_tracking(level, index, start, end, gap):
    global count

    if count != 0:
        return

    ans[level] = index

    if level > k:
        count += 1
        for i in range(1, k + 2):
            print(ans[i], end='')
        print()
        return


    for i in range(start, end, gap):
        if visited[i]:
            continue

        if level >= 1:
            s = str(ans[level]) + op[level - 1] + str(i)
            if not eval(s):
                continue

        visited[i] = 1
        back_tracking(level + 1, i, start, end, gap)
        visited[i] = 0

k = int(input())
op = list(input().split())
visited = [0 for _ in range(10)]
ans = [0  for _ in range(k + 2)]
count = 0

back_tracking(0, 0, 9, -1, -1)

visited = [0 for _ in range(10)]
ans = [0  for _ in range(k + 2)]
count = 0
back_tracking(0, 0, 0, 10, 1)
