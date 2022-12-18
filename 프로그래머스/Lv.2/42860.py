def solution(name):
    answer = 0
    alpha = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dic = {a: i for i, a in enumerate(alpha)}
    min_distance = len(name) - 1
    
    for i, n in enumerate(name):
        if n <= 'N':
            answer += dic[n]
        else:
            answer += (26 - dic[n])
            
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존, A 왼쪽, A 오른쪽
        min_distance = min([min_distance, 2 * i + len(name) - next,  2 * (len(name) - next) + i])
    answer += min_distance
    return answer