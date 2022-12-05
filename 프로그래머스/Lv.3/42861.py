import heapq
import sys
INF = sys.maxsize

def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    selected = [0]
    selected_node = 0
    candidate = []
    count = 0
    
    if n == 1:
        return costs[0][2]
    
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))

    while count < (n - 1):
        for g, cost in graph[selected_node]:
            if g not in selected:
                candidate.append((cost, g))
        heapq.heapify(candidate)
        cost, node = heapq.heappop(candidate)
        while node in selected:
            cost, node = heapq.heappop(candidate)
        print(node)
        selected.append(node)
        selected_node = node
        answer += cost
        count += 1
    return answer