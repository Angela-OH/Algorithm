def solution(s):
    alpha = s.lower().split(' ')
    for i in range(len(alpha)):
        if not alpha[i]:
            continue
        if alpha[i][0].isdigit():
            continue
        alpha[i] = alpha[i].replace(alpha[i][0], alpha[i][0].upper(), 1)
    answer = ' '.join(a for a in alpha)
    return answer