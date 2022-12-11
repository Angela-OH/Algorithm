from itertools import combinations

def isContain(lists, element):
    for list in lists:
        length = len(list)
        count = 0
        for e in element:
            for l in list:
                if e == l:
                    count += 1
        if count == length:
            return True
    return False

def isCandidate(relation, columns):
    row = []
    for i in range(len(relation)):
        column = []
        for j in columns:
            column.append(relation[i][j])
        row.append(column)

    if len(row) == len(set([tuple(r) for r in row])):
        return True
    else:
        return False

def solution(relation):
    answer = 0
    index = [i for i in range(len(relation[0]))]
    answer_list = []
    for i in range(1, len(relation[0]) + 1):
        for j in list(combinations(index, i)):
            if not isContain(answer_list, j):
                if isCandidate(relation, list(j)):
                    answer += 1
                    answer_list.append(j)
    return answer