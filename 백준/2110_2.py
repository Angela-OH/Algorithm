import sys

def binary_search(start, end):
    result = []
    while start <= end:
        mid = (start + end) // 2
        current = arr[0] # 시작점
        count = 1 # 0번 index에 공유기 1개 설치
        for i in arr: 
            if current + mid <= i:
                current = i
                count += 1
        if count >= c:
            start = mid + 1
            result.append(mid)
        else:
            end = mid - 1

    return max(result)

n, c = map(int, sys.stdin.readline().split())
arr = [[0] for _ in range(n)]
for i in range(n):
    arr[i] = int(sys.stdin.readline())
arr.sort()

start, end = 1, arr[n - 1] - arr[0]
print(binary_search(start, end))