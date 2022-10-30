import sys
sys.setrecursionlimit(10**6)

def find(k):
    if arr[k] == k:
        return k
    else:
        arr[k] = find(arr[k])
        return arr[k]

def union(i, j):
    i, j = find(i), find(j)
    if i != j:
        arr[i] = j

n = int(input())
m = int(input())
input_v = [list(map(int, input().split())) for _ in range(n)]
arr = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if i >= j :
            continue
        if input_v[i][j] == 1:
            union(i, j)

route = list(map(int, input().split()))
for i in range(m):
    route[i] -= 1
route = set(route)

count = 0
isPossible = 0

for r in route:
    result = find(r)
    if count == 0:
        compare = result
    else:
        if compare != result:
            isPossible = 1
            break
    count += 1
    
if isPossible:
    print("NO")
else:
    print("YES")

