import sys
input = sys.stdin.readline

def find(k):
    if parent[k] == k:
        return k
    else:
        parent[k] = find(parent[k])
        return parent[k]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return True
    else:
        parent[x] = y
        return False

n, m = map(int, input().split())
edge = []
parent = [i for i in range(n + 1)]
count, sum = 0, 0
for i in range(m):
    edge.append(list(map(int, input().split())))
edge.sort(key = lambda x : x[2])

for a, b, c in edge:
    if union(a, b):
        continue
    else:
        count += 1
        sum += c
    if count >= n - 2:
        break

print(sum)