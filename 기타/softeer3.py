import sys
input = sys.stdin.readline

p, n = map(int, input().split())
answer = 0
for v in list(map(int, input().split())):
    answer = (answer * p) % 1000000007 + v

print(answer)