import sys
ans = [0 for i in range(7)]

def back_tracking(n, arr, level, index):
    global ans
    ans[level] = arr[index]
    if level == 6:
        for i in range(1, 7):
            print(ans[i], end=" ")
        print()
        return
    if index == n:
        return

    for i in range(index + 1, n + 1):
        if (6 - level) > (n - index):
            continue
        back_tracking(n, arr, level + 1, i)
    
while True:
    input_text = list(map(int, sys.stdin.readline().strip().split()))
    n = input_text[0]
    if n == 0:
        break

    back_tracking(n, input_text, 0, 0)
    print()