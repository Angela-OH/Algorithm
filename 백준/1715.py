import sys, heapq
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
answer = 0

heapq.heapify(num)

while len(num) > 1:
    a, b = heapq.heappop(num), heapq.heappop(num)
    val = a + b
    heapq.heappush(num, val)
    answer += val

print(answer)