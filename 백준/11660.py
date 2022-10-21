import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]
arr[0] = [0 for _ in range(n + 1)]
sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    arr[i].insert(0, 0)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum [i - 1][j - 1] + arr[i][j]
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sum[x2][y2] - (sum[x1 - 1][y2] + sum[x2][y1 - 1]) + sum[x1 - 1][y1 - 1])