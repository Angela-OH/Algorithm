import sys
input = sys.stdin.readline

def binary_search(val):
    start, end = 0, len(lis)
    while start < end:
        mid = (start + end) // 2
        if val <= lis[mid]:
            end = mid
        else:
            start = mid + 1
    return start 

stock = []
while True:
    try:
        n = int(input())
        stock.append(list(map(int, input().split())))
    except:
        break

for i in range(len(stock)):
    lis = [stock[i][0]]
    for j in range(1, len(stock[i])):
        if lis[-1] < stock[i][j]:
            lis.append(stock[i][j])
        else:
            lis[binary_search(stock[i][j])] = stock[i][j]
    print(len(lis))