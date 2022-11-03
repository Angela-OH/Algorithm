def solution(n):
    answer = 0
    index = 1
    while True:
        start_num = n / index - (index - 1) / 2
        if start_num - int(start_num) == 0:
            answer += 1
        if start_num <= 1:
            break
        index += 1
    return answer