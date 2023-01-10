import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()

answer = 0
for i in range(n):
    left, right = 0, n - 1
    while left < right:
        val = num[left] + num[right]
        if num[i] == val:
            if i != left and i != right:
                answer += 1
                break
            elif i == left:
                left += 1
            else:
                right -= 1
        elif num[i] < val:
            right -= 1 # 값이 작아지게
        else:
            left += 1 # 값이 커지게

print(answer)