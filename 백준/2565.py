import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, len(lis)
    while start < end:
        mid = (start + end) // 2
        if lis[mid] < target: # 겹치는 수 없음
            start = mid + 1
        else:
            end = mid

    return start

n = int(input())
con = [[] for _ in range(n)]
lis = []
for i in range(n):
    con[i] = list(map(int, input().split()))
con.sort()
lis.append(con[0][1])

for i in range(1, n):
    if con[i][1] > lis[-1]:
        lis.append(con[i][1])
    lis[binary_search(con[i][1])] = con[i][1]

print(n - len(lis))


