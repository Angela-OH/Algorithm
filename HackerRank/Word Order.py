# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.readline
n = int(input())
arr = []
dic = {}
for i in range(n):
    s = input().strip()
    arr.append(s)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

arr = list(set(arr))

m = len(dic)
print(m)
for i in range(m):
    print(dic[arr[i]], end = ' ')