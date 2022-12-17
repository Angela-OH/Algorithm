def solution(k, d):
    answer = 0
    for x in range(d // k + 1):
        answer += int((d ** 2 / k ** 2 - x ** 2) ** 0.5)
        answer += 1
    return answer