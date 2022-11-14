def solution(participant, completion):
    dict = {}
    answer = ''
    
    for p in participant:
        dict[p] = dict.get(p, 0) + 1
    
    for c in completion:
        dict[c] -= 1
    
    for d in dict:
        if dict[d] != 0:
            answer = d
            
    return answer