import sys
input = sys.stdin.readline

def person(mid):
    p = 0
    for i in range(n):
        p += (mid // time[i])
    return p

def binary_search(start, end):
    while start < end:
        mid = (start + end) // 2
        if person(mid) >= m:
            end = mid
        else:
            start = mid + 1
    return start

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]
min_time, max_time = 1, max(time) * m

print(binary_search(min_time, max_time))