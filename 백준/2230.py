import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))
num.sort()
start, end = 0, 0
answer = num[-1] - num[0]
while end < n and start <= end:
    val = abs(num[start] - num[end])
    if val < m:
        end += 1
    else:
        if val < answer:
            answer = val
        start += 1

print(answer)  