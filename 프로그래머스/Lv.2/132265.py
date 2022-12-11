def solution(topping):
    answer = 0
    bro1, bro2 = {}, {}
    for t in topping:
        if t in bro1:
            bro1[t] += 1
        else:
            bro1[t] = 1
    for i in range(len(topping) - 1):
        top = topping[i]
        if bro1[top] == 1:
            del bro1[top]
        else:
            bro1[top] -= 1
        if top in bro2:
            bro2[top] += 1
        else:
            bro2[top] = 1
        if len(bro1) == len(bro2):
            answer += 1
    return answer      