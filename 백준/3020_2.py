import sys

n, h = map(int, sys.stdin.readline().split())
arr1 = [0 for _ in range(h + 2)]
arr2 = [0 for _ in range(h + 2)]
count = [0 for _ in range(h)]

for i in range(n):
    obstacle = int(sys.stdin.readline())
    if i % 2 == 0:
        arr1[obstacle] += 1
    else:
        arr2[obstacle] += 1

for i in range(h, 1, -1):
    arr1[i - 1] += arr1[i]
    arr2[i - 1] += arr2[i]

for i in range(h):
    count[i] = arr1[i + 1] + arr2[h - i]

min_val = min(count)
print(min_val, end = ' ')
print(count.count(min_val))