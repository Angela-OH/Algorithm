n = int(input())
k = int(input())

low, high = 1, k
answer = 0
while low <= high:
    count = 0
    mid = (low + high) // 2
    
    for i in range(1, n + 1):
        count += min(mid // i, n)
    
    if count >= k:
        answer = mid
        high = mid -1
    else:
        low = mid + 1

print(answer)