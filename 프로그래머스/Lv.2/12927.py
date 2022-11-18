import heapq

def solution(n, works):
    answer = 0
    works = [-1 * i for i in works]
    heapq.heapify(works)
    
    for i in range(n):
        result = heapq.heappop(works)
        if result == 0:
            heapq.heappush(works, result)
        else:
            heapq.heappush(works, result + 1)
    for w in works:
        answer += pow(w, 2)
        
    return answer