def check():
    sum = 0
    for i in range(2, n + 1):
        sum += abs(ans[i - 1] - ans[i])
    return sum

def back_tracking(level, index):
    global max
    
    if level != 0:
        ans[level] = arr[index]

    if level == n:
        sum = check()
        if sum > max:
            max = sum
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        back_tracking(level + 1, i)
        visited[i] = 0

n = int(input())
arr = list(map(int, input().split()))
visited = [0 for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]
max = 0

back_tracking(0, 0)

print(max)