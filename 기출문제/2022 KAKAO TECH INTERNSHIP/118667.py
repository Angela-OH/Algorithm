from collections import deque

def solution(queue1, queue2):
    answer = 0
    s1, s2 = sum(queue1), sum(queue2)
    length = len(queue1)
    queue1, queue2 = deque(queue1), deque(queue2)
    
    if (s1 + s2) % 2 != 0:
        return -1
    
    while s1 != s2:
        if answer > 4 * length:
            return -1
        if s1 > s2:
            val = queue1.popleft()
            queue2.append(val)
            s1 -= val
            s2 += val
        else:
            val = queue2.popleft()
            queue1.append(val)
            s1 += val
            s2 -= val
        answer += 1
        
    return answer

print(solution([1, 10, 1, 2], [1, 2, 1, 2]))