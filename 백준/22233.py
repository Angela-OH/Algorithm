import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}
post = [[] for _ in range(m)]

for i in range(n):
    memo[input().strip()] = 1

left = n
for i in range(m):
    for keyword in list(input().strip().split(',')):
        if keyword in memo:
            if memo[keyword] == 1:
                memo[keyword] = 0
                if left > 0:
                    left -= 1
    print(left)

