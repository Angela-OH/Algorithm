import sys
sys.setrecursionlimit(10**6)

def find(k):
    if arr[k] == k:
        return k
    else:
        arr[k] = find(arr[k])
        return arr[k]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return True
    else:
        arr[a] = b
        return False

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(n)]
count = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if union(a, b):
        if count == 0:
            count = i + 1

print(count)