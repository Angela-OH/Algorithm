def solution(id_list, report, k):
    n = len(id_list)
    answer = [0 for _ in range(n)]
    user = {}
    for i, id in enumerate(id_list):
        user[id] = i
    issued = [[False for _ in range(n)] for _ in range(n)]
    num = {id: 0 for id in id_list}
    
    for r in report:
        r = r.split()
        if issued[user[r[0]]][user[r[1]]]: 
            continue
        num[r[1]] += 1
        issued[user[r[0]]][user[r[1]]] = True
        
    for i in range(n):
        for j in range(n):
            if issued[i][j] and num[id_list[j]] >= k:
                answer[i] += 1
    
    ''' set을 쓰면 메모리를 아낄 수 있음
    for r in set(report):
        num[r.split()[1]] += 1
    
    for r in set(report):
        r = r.split()
        if num[r[1]] >= k:
            answer[user[r[0]]] += 1
    '''

    return answer