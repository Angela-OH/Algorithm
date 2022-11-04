def solution(n, words):
    dic = {}
    index, rnd = 0, 0
    for i in range(len(words)):
        if words[i] in dic:
            index = i % n + 1
            rnd = i // n + 1
            break
        else:
            dic[words[i]] = 1
        if i > 0:
            if words[i][0] != words[i-1][-1]:
                index = i % n + 1
                rnd = i // n + 1
                break
    answer = [index, rnd]
    return answer