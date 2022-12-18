''' 정확도 OK, 효율성 NO
def solution(board, skill):
    answer = 0
    dic = {1: -1, 2: 1}
    for s in skill:
        typ, x1, y1, x2, y2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
        typ = dic[typ]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] += typ * degree    
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
                
    return answer
'''

def solution(board, skill):
    answer = 0
    dic = {1: -1, 2: 1}
    sum = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for s in skill:
        typ = dic[s[0]]
        x1, y1, x2, y2 = s[1], s[2], s[3], s[4]
        degree = s[5]
        sum[x1][y1] += (typ * degree)
        sum[x2 + 1][y2 + 1] += (typ * degree)
        sum[x1][y2 + 1] += (-typ * degree)
        sum[x2 + 1][y1] += (-typ * degree)
    
    for i in range(len(board[0])):
        for j in range(1, len(board)):
            sum[j][i] += sum[j - 1][i]
    for i in range(len(board)):
        for j in range(1, len(board[0])):
            sum[i][j] += sum[i][j - 1]
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + sum[i][j] > 0:
                answer += 1
    return answer