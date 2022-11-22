from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0 for _ in range(bridge_length)])
    sum = 0
    while queue:
        sum -= queue.popleft()
        answer += 1
        if truck_weights:
            if truck_weights[0] + sum <= weight:
                queue.append(truck_weights[0])
                sum += truck_weights[0]
                del truck_weights[0]
            else:
                queue.append(0)
    
    return answer