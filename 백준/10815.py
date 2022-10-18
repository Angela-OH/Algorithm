import sys

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == target:
            return 1
        elif arr1[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return 0

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for arr in arr2:
    print(binary_search(0, n - 1, arr), end = ' ')
