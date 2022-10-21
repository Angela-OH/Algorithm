import sys

def binary_search(start, end):
    global max_val
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for a in arr:
            sum += (a // mid)
        if sum >= k:
            if mid > max_val:
                max_val = mid
            start = mid + 1
        else:
            end = mid - 1

n, k = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(sys.stdin.readline())
max_val = 0

binary_search(1, max(arr))

print(max_val)