import sys

def binary_search(target):
    start, end = 0, len(lis) - 1
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lis = [arr[0]]

for i in range(1, n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        lis[binary_search(arr[i])] = arr[i]

print(len(lis))
