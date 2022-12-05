import sys
INF = sys.maxsize

def solution(N, road, K):
    answer = 0
    count = 0
    choose = 0
    graph = [[INF for _ in range(N)] for _ in range(N)]
    dp = [INF for _ in range(N)]
    visited = [0 for _ in range(N)]
    dp[0] = 0
    visited[0] = 1
    
    for r in road:
        graph[r[0] - 1][r[1] - 1] = min(graph[r[0] - 1][r[1] - 1], r[2])
        graph[r[1] - 1][r[0] - 1] = min(graph[r[1] - 1][r[0] - 1], r[2])
    
    for i in range(N):
        graph[i][i] = 0
        
    while count < (N - 1):
        min_v, min_i = INF, 0
        for i in range(1, N):
            if visited[i] == 1:
                continue
            dp[i] = min(dp[i], dp[choose] + graph[choose][i])
            if dp[i] < min_v:
                min_v = dp[i]
                min_i = i
        choose = min_i
        visited[min_i] = 1
        count += 1
        
    for d in dp:
        if d <= K:
            answer += 1
            
    return answer