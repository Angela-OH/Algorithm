def solution(clothes):
    answer = 1
    dic = {}
    for name, type in clothes:
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
    
    for d in dic.items():
        answer *= (d[1] + 1)
    
    return answer - 1