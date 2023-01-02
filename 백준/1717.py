import sys
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: # 같은 집합
        return
    if parent[x] < parent[y]: # x가 높이가 더 높은 트리를 구성
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

n, m = map(int, input().split())
parent = [-1 for _ in range(n + 1)]
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # 합집합으로 만듦
        union(a, b)
    else: # 두 원소가 같은 집합에 포함되어 있는가? (Y/N 출력)
        a, b = find(a), find(b)
        if a == b:
            print("YES")
        else:
            print("NO")