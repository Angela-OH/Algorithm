import sys

def search(arr, target):
    start, end = 0, index - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start
        
n, h = map(int, sys.stdin.readline().split())
index = n // 2
arr1 = [0 for _ in range(index)]
arr2 = [0 for _ in range(index)]
ans = [0 for _ in range(h)]
min = 200000
count = 0

for i in range(n):
    obstacle = int(sys.stdin.readline())
    if i % 2 == 0:
        arr1[i//2] = obstacle
    else:
        arr2[i//2] = obstacle

arr1.sort()
arr2.sort()

for i in range(h):
    bottom = index - search(arr1, i)
    top = index - search(arr2, h - 1 - i)
    num = bottom + top

    if num < min:
        min = num
        count = 0
    if num == min:
        count += 1

print(min, end = ' ')
print(count)