def decision(typ, a, b):
    if typ[a] >= typ[b]:
        return a
    else:
        return b

def solution(survey, choices):
    answer = ''
    typ = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N":0}
    
    for i in range(len(survey)):
        if choices[i] < 4: # 비동의
            typ[survey[i][0]] += (4 - choices[i]) 
        elif choices[i] > 4: # 동의
            typ[survey[i][1]] += (choices[i] - 4)
    
    # 지표 1: R/T
    answer += decision(typ, 'R', 'T')
    # 지표 2: C/F
    answer += decision(typ, 'C', 'F')
    # 지표 3: J/M
    answer += decision(typ, 'J', 'M')
    # 지표 4: A/N
    answer += decision(typ, 'A', 'N')
    
    return answer