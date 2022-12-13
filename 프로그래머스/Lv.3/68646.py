from itertools import combinations
import sys
INF = sys.maxsize

def solution(a):
    answer = 2
    n = len(a)
    min_left = [INF for _ in range(n)]
    min_left[0] = a[0]
    min_right = [INF for _ in range(n)]
    min_right[-1] = a[-1]
    for i in range(1, n):
        min_left[i] = min(min_left[i - 1], a[i])
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], a[i])
    for i in range(1, n - 1):
        left = min_left[i - 1]
        right = min_right[i + 1]
        if (left < a[i] < right) or (right < a[i] < left) or (a[i] < left and a[i] < right):
            answer += 1
    return answer