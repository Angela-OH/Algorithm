import heapq

def solution(operations):
    answer = []
    min_heap, max_heap = [], []
    for operation in operations:
        operation = operation.split(" ")
        op, num = operation[0], int(operation[1])
        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -1 * num)
        else:
            if not min_heap:
                continue
            if num < 0: # 최솟값
                result = heapq.heappop(min_heap)
                del max_heap[max_heap.index(-1 * result)]
            else: # 최댓값
                result = heapq.heappop(max_heap)
                del min_heap[min_heap.index(-1 * result)]
    if min_heap:
        answer = [heapq.heappop(max_heap) * -1, heapq.heappop(min_heap)]
    else:
        answer = [0, 0]
        
    return answer