from collections import deque

def solution(order):
    answer = 0
    n = len(order)
    belt = [i + 1 for i in range(n)]
    queue = deque([])
    belt_idx, order_idx = 0, 0
    while belt_idx < n or queue:
        if belt_idx < n and order[order_idx] == belt[belt_idx]:
            answer += 1
            belt_idx += 1
            order_idx += 1
        elif not queue :
            queue.append(belt[belt_idx])
            belt_idx += 1
        elif order[order_idx] == queue[-1]:
            answer += 1
            order_idx += 1
            queue.pop()
        else:
            if belt_idx >= n:
                break
            queue.append(belt[belt_idx])
            belt_idx += 1
    return answer