import sys
input = sys.stdin.readline

n = int(input())
answer = 0
info = [[] for _ in range(4)]
ab, cd = {}, {}

for i in range(n):
    a, b, c, d = map(int, input().split())
    info[0].append(a)
    info[1].append(b)
    info[2].append(c)
    info[3].append(d)

# A, B 배열 합
for i in range(n):
    for j in range(n):
        val = info[0][i] + info[1][j]
        if val in ab.keys():
            ab[val] += 1
        else:
            ab[val] = 1

# C, D 배열 합
for i in range(n):
    for j in range(n):
        val = -1 * (info[2][i] + info[3][j])
        if val in ab.keys():
            answer += ab[val]

print(answer)