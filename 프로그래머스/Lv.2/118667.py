from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    count = 0
    queue_sum = sum1 + sum2
    if queue_sum % 2 != 0:
        return -1
    
    while True:
        if count == len(queue1) * 4:
            answer = -1
            break
        if sum1 == sum2:
            break
        elif sum1 > sum2:
            pop = queue1.popleft()
            sum1 -= pop
            queue2.append(pop)
            sum2 += pop
        else:
            pop = queue2.popleft()
            sum2 -= pop
            queue1.append(pop)
            sum1 += pop
        answer += 1
        count += 1
    return answer