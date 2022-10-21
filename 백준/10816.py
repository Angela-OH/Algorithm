import sys

def upper_bound(target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr_n[mid] <= target:
            start = mid + 1
        else:
            end = mid -1
    return start

def lower_bound(target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr_n[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
arr_n.sort()

m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

for arr in arr_m:
    print(upper_bound(arr) - lower_bound(arr), end = ' ')
