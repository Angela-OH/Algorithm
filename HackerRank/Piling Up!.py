# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt, num = 0, 2 ** 31
    
    while arr:
        left, right = arr[0], arr[-1]
        if num < max(left, right):
            cnt = 1
            break
        if left <= right:
            num = right
            del arr[-1]
        else:
            num = left
            del arr[0]
        
    if cnt == 0:
        print("Yes")
    else:
        print("No")