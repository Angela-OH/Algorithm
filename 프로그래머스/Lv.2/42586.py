import math

def solution(progresses, speeds):
    deploy = [0 for _ in range(len(progresses))]
    dic = {}
    
    for i in range(len(progresses)):
        deploy[i] = math.ceil((100 - progresses[i]) / speeds[i])
    
    for i in range(1, len(deploy)):
        if deploy[i] < deploy[i - 1]:
            deploy[i] = deploy[i - 1]
    
    for d in deploy:
        if d in dic:
            dic[d] += 1
        else:
            dic[d] = 1
    
    answer = [b for a, b in sorted(dic.items())]
    
    return answer