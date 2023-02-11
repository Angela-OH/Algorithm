import sys
from collections import deque
input = sys.stdin.readline

n, m, c = map(int, input().split())
pref = [list(map(int, input().split())) for _ in range(c)]
if n > m:
    temp = n
    n = m
    m = temp
    b = list(map(int, input().split()))
    a = list(map(int, input().split()))
else:
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))

queue = deque([])
answer = 0

a_idx, b_idx = 0, 0
queue.append((-1, -1, 0))
while queue:
    a_idx, b_idx, cnt = queue.popleft()
    answer = max(answer, cnt)
    a_idx += 1
    if a_idx == n:
        continue
    b_idx += 1
    if b_idx == m:
        continue
    queue.append((a_idx, b_idx - 1, cnt))
    for i in range(b_idx, m):
        if a_idx >= i:
            queue.append((a_idx, i, cnt + pref[a[a_idx] - 1][b[i] - 1]))

print(answer)