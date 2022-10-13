count = 0
def back_tracking(n, index, choose, sum):
    global count

    if index >= n:
        return

    if choose == 1:
        sum += p[index]
        if sum == s:
            count += 1

    back_tracking(n, index + 1, 0, sum) # 선택 안 함
    back_tracking(n, index + 1, 1, sum) # 선택 함

n, s = map(int, input().split())
p = list(map(int, input().split()))
visited = [0 for i in range(n)]
back_tracking(n, 0, 0, 0)
back_tracking(n, 0, 1, 0)
print(count)
