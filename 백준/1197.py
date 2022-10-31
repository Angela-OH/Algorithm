import sys

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

v, e = map(int, sys.stdin.readline().split())
edge = []
parent = [i for i in range(v)]
count, sum = 0, 0
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((c, a - 1, b - 1))

edge.sort(key = lambda x: x[0])

for c, a, b in edge:
    if union(a, b):
        continue
    else:
        count += 1
        sum += c

    if count >= v - 1:
        break

print(sum)