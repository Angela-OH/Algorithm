import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = list(map(int, input().split()))
isSmall = [False for _ in range(n)]
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    if w[a - 1] < w[b - 1]:
        isSmall[a - 1] = True
    elif w[a - 1] == w[b - 1]:
        isSmall[a - 1] = True
        isSmall[b - 1] = True
    else:
        isSmall[b - 1] = True

for i in range(n):
    if not isSmall[i]:
        answer += 1

print(answer)
