def binary_search(times, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in times:
            count += (mid // time)
            
        if count >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def solution(n, times):
    start, end = 1, max(times) * n
    answer = binary_search(times, start, end, n)
    return answer