import sys
INF = sys.maxsize

def solution(n, results):
    answer = 0
    info = [[0 for _ in range(n)] for _ in range(n)] # 0은 결과를 모름
    for result in results:
        info[result[0] - 1][result[1] - 1] = 1 # 1은 이김
        info[result[1] - 1][result[0] - 1] = -1 # -1은 짐

    for i in range(n):
        for j in range(n):
            for k in range(n): # j vs k
                if info[j][i] == 0:
                    continue
                    
                # 1 vs 2, 2 vs 3 정보를 가지고 1 vs 3 비교
                # 1 < 2, 2 < 3 => 1 < 3
                # but if 1 < 2, 2 > 3 => 비교 불가
                if info[j][i] == info[i][k]:
                    info[j][k] = info[j][i]
                    info[k][j] = -1 * info[j][i]

    for i in range(n):
        if info[i].count(0) == 1:
            answer += 1
            
    return answer