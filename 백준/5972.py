import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    distance = [INF for _ in range(n)]
    distance[0] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a - 1].append([b - 1, c])
        graph[b - 1].append([a - 1, c])
    
    heap = []
    heapq.heappush(heap, (0, 0)) # 현서의 위치
    while heap:
        dis, node = heapq.heappop(heap)
        for g in graph[node]:
            new_node, new_dis = g[0], g[1] + dis
            if new_dis < distance[new_node]:
                distance[new_node] = new_dis
                heapq.heappush(heap, (new_dis, new_node))
    print(distance[n - 1])