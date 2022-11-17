def seperate(file):
    isHead, isNumber, isTail = 0, 0, 0
    head, number, tail = '', '', ''
    cnt = 0
    for i in range(len(file)):
        if not file[i].isdigit() and isHead == 0:
            head += file[i]
        elif file[i].isdigit() and isNumber == 0 and cnt <= 5:
            isHead = 1
            cnt += 1
            number += file[i]
        else:
            isNumber = 1
            tail += file[i]
    return (head, number, tail)

def solution(files):
    answer = []
    dic = {}
    for index, file in enumerate(files):
        head, number, tail = seperate(file)
        head = head.lower()
        number = int(number)
        if head in dic:
            if number in dic[head]:
                dic[head][number].append((tail, index))
            else:
                dic[head][number] = [(tail, index)]
        else:
            dic[head] = {number: [(tail, index)]}

    for key in dic:
        dic[key] = sorted(dic[key].items(), key = lambda x: x[0])
    dic = sorted(dic.items(), key = lambda x: x[0])

    for head, value in dic:
        for num, tail in value:
            for t in tail:
                answer.append(files[t[1]])
    return answer