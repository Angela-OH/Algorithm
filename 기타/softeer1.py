import sys, heapq
input = sys.stdin.readline

w, n = map(int, input().split())
info = []
cnt, answer = 0, 0
for i in range(n):
    m, p = map(int, input().split())
    info.append((-p, m))
heapq.heapify(info)

while len(info) > 0:
    p, m = heapq.heappop(info)
    p *= -1
    if m <= (w - cnt):
        cnt += m
        answer += (p * m)
    else:
        answer += p * (w - cnt)
        break

print(answer)