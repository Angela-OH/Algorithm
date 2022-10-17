def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in range(n):
            if arr[i] < mid:
                sum += arr[i]
            else:
                sum += mid
        if sum == m:
            return mid
        elif sum < m:
            result = mid
            start = mid +1
        else:
            end = mid -1

    return result

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())

print(binary_search(0, arr[n - 1]))
