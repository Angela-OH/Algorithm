def solution(want, number, discount):
    answer = 0
    dic = {}
    for i, w in enumerate(want):
        dic[w] = number[i]

    for i in range(len(discount) - 10 + 1):
        tmp = {}
        for j in range(i, i + 10):
            if discount[j] in tmp:
                tmp[discount[j]] += 1
            else:
                tmp[discount[j]] = 1
        if tmp == dic:
            answer += 1
        
    return answer