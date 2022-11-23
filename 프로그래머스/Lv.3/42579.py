def solution(genres, plays):
    answer = []
    dic = {}
    for i, g in enumerate(genres):
        if g in dic:
            dic[g].append([plays[i], i])
            dic[g][0][0] += plays[i]
        else:
            dic[g] = [[plays[i], -1]]
            dic[g].append([plays[i], i])
    
    for d in dic:
        dic[d].sort(reverse = True, key = lambda x: (x[0], -x[1]))
        if len(dic[d]) > 3:
            dic[d] = dic[d][:3]

    for i in sorted(dic.values(), reverse = True):
        for j in i:
            if j[1] == -1:
                continue
            answer.append(j[1])
            
    return answer