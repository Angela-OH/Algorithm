def check(s, n):
    new_s = ''
    index, count = 0, 1
    while index < len(s):
        next_index = index + n
        if s[index: next_index] == s[next_index: next_index + n]:
            count += 1
        else:
            if count > 1:
                new_s += str(count)
                count = 1
            new_s += s[index: next_index]
        index = next_index
    return len(new_s)

def solution(s):
    answer = 1000
    count = 0
    for i in range(len(s)//2, 0, -1):
        length = check(s, i)
        if length < answer:
            answer = length
            count += 1
    if count == 0:
        answer = 1
    return answer