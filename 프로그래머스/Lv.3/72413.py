import sys
INF = sys.maxsize

def solution(n, s, a, b, fares):
    answer = INF
    board = [[INF for _ in range(n)] for _ in range(n)]
    for c, d, f in fares:
        board[c - 1][d - 1] = f
        board[d - 1][c - 1] = f
    for i in range(n):
        board[i][i] = 0
        
    for i in range(n): # 중간에 지나칠 지점
        for j in range(n): # 출발지점
            for u in range(n): # 도착지점
                board[j][u] = min(board[j][u], board[j][i] + board[i][u])
    
    for i in range(n):
        share = board[s - 1][i] + board[i][a - 1] + board[i][b - 1]
        if share < answer:
            answer = share
    if board[s - 1][a - 1] + board[s - 1][b - 1] < answer:
        answer = board[s - 1][a - 1] + board[s - 1][b - 1]
        
    return answer