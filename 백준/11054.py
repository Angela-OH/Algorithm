import sys
input = sys.stdin.readline

def binary_search(r, target): 
    start, end = 0, len(r)

    while start < end:
        mid = (start + end) // 2
        if r[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

def lis(num):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    r = [num[0]]

    for i in range(1, n):
        if num[i] > r[-1]:
            r.append(num[i])
        else:
            r[binary_search(r, num[i])] = num[i]
        dp[i] = len(r)   

    return dp

n = int(input())
num = list(map(int, input().split()))
answer = 1

asc = lis(num)
des = lis(num[::-1])
des = des[::-1]

for i in range(n - 1):
    answer = max(answer, asc[i] + des[i] - 1)

print(answer)