# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
answer = 0

for arr in array:
    if arr in a:
        answer += 1
    if arr in b:
        answer -= 1
    
print(answer)
