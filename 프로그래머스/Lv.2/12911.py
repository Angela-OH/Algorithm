def solution(n):
    bin_n = format(n, 'b')
    one_cnt = bin_n.count('1')
    while True:
        n += 1
        if one_cnt == format(n, 'b').count('1'):
            answer = n
            break
    return answer