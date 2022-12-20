import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [0 for _ in range(n)]
select = {}
max = 0
for i in range(n):
    belt[i] = int(input())

for i in range(k):
    if belt[i] in select:
        select[belt[i]] += 1
    else:
        select[belt[i]] = 1

for i in range(1, n):
    old = belt[i - 1]
    if select[old] == 1:
        del select[old]
    else:
        select[old] -= 1

    new = belt[(i - 1 + k) % n]
    if new in select:
        select[new] += 1
    else:
        select[new] = 1
    
    sum = len(select)
    if c not in select:
        sum += 1
    
    if sum > max:
        max = sum

print(max)