def compare(tmp, skill):
    length = len(tmp)
    for i in range(length):
        if skill[i] != tmp[i]:
            return False
    return True
            
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        tmp = ''
        for s in skills:
            if s in skill:
                tmp += s
        if compare(tmp, skill):
            answer += 1
    return answer