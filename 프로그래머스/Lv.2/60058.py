def isFine(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True

def divide(w): # 문자열 w를 u, v로 분리
    c1, c2 = 0, 0
    index = 0
    for i, v in enumerate(w):
        if v == '(':
            c1 += 1
        else:
            c2 += 1
        if c1 == c2:
            index = i
            break
    return (w[:index + 1], w[index + 1:])

def solution(p):
    if not p:
        return ''
    u, v = divide(p)
    if isFine(u): # u가 올바른 괄호 문자열?
        u += solution(v)
        return u
    else:
        s = '('
        s += solution(v)
        s += ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                s += ')'
            else:
                s += '('
        return s