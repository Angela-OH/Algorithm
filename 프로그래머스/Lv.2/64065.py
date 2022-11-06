def solution(s):
    answer = []
    dic = {}
    s = s.replace('}', '').replace('{', '').split(',')
    for a in s:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 0
            
    answer = list(map(int, [k for k, v in sorted(dic.items(), key = lambda x: -x[1])]))

    return answer