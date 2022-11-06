def check(s):
    stack = []
    dic = {')': '(', '}': '{', ']': '['}
    for a in s:
        if a in [')', '}', ']']:
            if not stack:
                return False
            if dic[a] != stack.pop():
                return False
        else:
            stack.append(a)
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    for x in range(len(s)):
        if check(s[x:] + s[:x]):
            answer += 1
    return answer