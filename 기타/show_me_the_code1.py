import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
answer = 1
start, end = 0, 0
left, right = 0, 0
if num[0] == 1:
    left = 1
else:
    right = 1

while end < n:
    checked = False
    answer = max(answer, abs(left - right))
    n_start, n_left, n_right = start, left, right
    while num[n_start] != num[end]: # 최적의 값이 나올 가능성이 더 있음
        if num[n_start] == 1:
            n_left -= 1
        else:
            n_right -= 1
        val = abs(n_left - n_right)
        if val >= answer:
            answer = val
            checked = True # 최적의 값으로 업데이트 됨
        n_start += 1

    if checked: # start를 조정해줘야함
        start, left, right = n_start, n_left, n_right

    if end < n - 1:
        end += 1
        if num[end] == 1:
            left += 1
        else:
            right += 1
    else:
        end += 1

print(answer)