import re
import itertools

def solution(expression):
    answer = 0
    p = re.compile('\W|\d+')
    m = p.findall(expression)
    op = list(set([m[i] for i in range(1, len(m), 2)]))
    for priorities in itertools.permutations(op, len(op)):
        result = 0
        tmp = m.copy()
        for priority in priorities:
            index = 1
            while index < len(tmp):
                if tmp[index] == priority:
                    num1 = tmp[index - 1]
                    op = tmp[index]
                    num2 = tmp[index + 1]
                    del tmp[index + 1]
                    del tmp[index]
                    del tmp[index - 1]
                    result = str(eval(num1 + op + num2))
                    tmp.insert(index - 1, result)
                else:
                    index += 2
        if abs(int(tmp[0])) > answer:
            answer = abs(int(tmp[0]))
    return answer