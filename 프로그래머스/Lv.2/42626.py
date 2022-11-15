import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville:
        heapq.heappush(heap, s)
        
    while heap:
        least = heapq.heappop(heap)
        if least >= K:
            break
        if len(heap) < 1:
            answer = -1
            break
        least_next = heapq.heappop(heap)
        heapq.heappush(heap, least + least_next * 2)
        answer += 1
    return answer