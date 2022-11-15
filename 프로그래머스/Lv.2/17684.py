from string import ascii_uppercase

def solution(msg):
    answer = []
    dic = {}
    for index, word in list(enumerate(ascii_uppercase)):
        dic[word] = index + 1
    
    i = 0
    while i < len(msg):
        result_index, tmp = 0, 0# 색인 번호 저장
        for j in range(i + 1, len(msg) + 1):
            if msg[i:j] in dic:
                result_index = dic[msg[i:j]]
                tmp = j
            else:
                dic[msg[i:j]] = len(dic) + 1
                break
        i = tmp
        answer.append(result_index)
                
    return answer