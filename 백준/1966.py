from collections import deque

def printer(arr, n, m):
    queue = deque([])
    count = 0

    for i in range(n):
        queue.append((i, arr[i]))
    
    while True:
        max_val = max(queue, key=lambda x:x[1])[1]
        index, priority = queue.popleft()
        if priority < max_val:
            queue.append((index, priority))
            continue
        count += 1
        if index == m:
            break
    
    return count

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(printer(arr, n, m))