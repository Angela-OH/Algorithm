def solution(n, info):
    info = info[::-1]
    m = len(info)
    answer = [0 for _ in range(m)]
    max_gap = 0
    min_sc = 0
    max_cnt = 0
    res = 0
    
    for i in range(1, (2 << m)):
        total = n
        sum = 0
        sc = 0
        cnt = 0
        isChecked = False
        isNext = False
        e_sum = 0
        for j in range(m):
            if (i & (1 << j)) != 0: # bit가 켜져있음
                if not isChecked:
                    isChecked = True
                    sc = j
                    cnt = info[j] + 1
                total -= (info[j] + 1) # 어피치보다는 큰 값을 가져야함
                sum += j
                if total < 0:
                    isNext = True
                    break
            else: # bit가 꺼져있음
                if info[j] > 0:
                    e_sum += j
        if isNext:
            continue
        gap = sum - e_sum
        if gap > max_gap:
            max_gap = gap
            min_sc = sc
            max_cnt = cnt
            res = i
        elif gap == max_gap:
            if sc < min_sc:
                min_sc = sc
                max_cnt = cnt
                res = i
            elif sc == min_sc:
                if cnt > max_cnt:
                    max_cnt = cnt
                    res = i
    
    if res == 0:
        answer = [-1]
        return answer
    
    total = n
    for i in range(m):
        if (res & (1 << i)) != 0:
            answer[i] = info[i] + 1
            total -= answer[i]
    if total > 0:
        answer[0] += total
        
    return answer[::-1]