def change_num(n, number):
    result = ''
    alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dic = {i: j for i, j in enumerate(alpha)}
    while number >= n:
        result = str(dic[number % n]) + result
        number = number // n
    result = str(dic[number]) + result
    return result

def combine_num(n, length):
    flow, index = '', 0
    while True:
        flow += change_num(n, index)
        if len(flow) >= length:
            return flow[:length]
        index += 1
    return flow

def solution(n, t, m, p):
    answer = ''
    length = m * (t - 1) + p
    flow = combine_num(n, length)
    print(flow)
    for i in range(p - 1, length, m):
        answer += flow[i]
    return answer