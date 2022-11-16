def solution(record):
    answer = []
    dic = {}
    for r in record:
        info = r.split(" ")
        if info[0] == 'Enter' or info[0] == 'Change':
            dic[info[1]] = info[2]
    
    for r in record:
        info = r.split(" ")
        if info[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[info[1]]))
        elif info[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(dic[info[1]]))
    
    return answer