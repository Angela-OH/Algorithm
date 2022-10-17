# 시간 초과
import sys

def dfs(start):
    stack = [(start, 0, 1000000001)]
    global max

    while stack:
        loc, level, dis = stack.pop()
        if level == (c - 1):
            if dis > max:
                max = dis
            continue
        if loc == (n - 1):
            continue
        for i in range(loc + 1, n):
            if dis > arr[i] - arr[loc]:
                new_dis = arr[i] - arr[loc]
            else:
                new_dis = dis
            stack.append((i, level + 1, new_dis))

n, c = map(int, sys.stdin.readline().split())
arr = [[0] for _ in range(n)]
for i in range(n):
    arr[i] = int(sys.stdin.readline())
arr.sort()
max = 0

for i in range(n):
    dfs(i)

print(max)