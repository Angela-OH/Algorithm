'''시도 1
def solution(stones, k):
    answer = 200000000
    for i in range(0, len(stones) - k + 1):
        time = max(stones[i: i + k])
        if time < answer:
            answer = time

    return answer
'''

'''시도 2
def solution(stones, k):
    answer = 200000000
    index = 0
    while index <= len(stones) - k:
        max = 0
        for i in range(index, index + k):
            if stones[i] >= max:
                max = stones[i]
                index = i
        if max < answer:
            answer = max
        index += 1

    return answer
'''
def solution(stones, k):
    left, right = min(stones), max(stones) # 건널 수 있는 인원의 min, max
    answer = 0
    while left <= right:
        mid = (left + right) // 2 # 건너는 인원
        empty_count = 0
        for s in stones:
            if s - mid <= 0:
                empty_count += 1 # 못 건너는 stone
            else:
                empty_count = 0 # 연속 x
                
            if empty_count >= k:
                break
                
        if empty_count >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left