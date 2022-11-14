import math

def solution(n, left, right):
    answer = []
    for i in range(left + 1, right + 2):
        x = math.ceil(i / n)
        if i % n == 0: y = n
        else: y = i % n
        answer.append(max(x, y))
    return answer