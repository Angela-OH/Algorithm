def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                answer = False
    if stack:
        answer = False
        
    return answer