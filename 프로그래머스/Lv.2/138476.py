def solution(k, tangerine):
    answer = 0
    size = {}
    for t in tangerine:
        if t in size:
            size[t] += 1
        else:
            size[t] = 1
            
    size = sorted(size.items(), key = lambda x: -x[1])
    
    for t, s in size:
        if k <= 0:
            break
        k -= s
        answer += 1
    return answer