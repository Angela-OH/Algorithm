import sys

def binary_search(l, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return start

def lis():
    l = [arr[0]]

    for i in range(1, n):
        if l[-1] < arr[i]:
            l.append(arr[i])
        else:
            idx = binary_search(l, 0, len(l) - 1, arr[i])
            l[idx] = arr[i]
    return len(l)

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

print(lis())
