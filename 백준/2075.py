import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    heap = []
    for i in range(n):
        for j in list(map(int, input().split())):
            if len(heap) >= n: # 메모리 조절
                if heap[0] < j: # 최소값보다 크면 최소값을 현재 값으로 변경
                    heapq.heappop(heap)
                    heapq.heappush(heap, j)
            else:
                heapq.heappush(heap, j)

    # print(heap[0]) 해도 됨
    
    heap = [-1 * i for i in heap]
    heapq.heapify(heap)

    for i in range(n - 1):
        heapq.heappop(heap)

    print(heapq.heappop(heap) * -1)