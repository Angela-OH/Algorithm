def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    camera = -30000
    for start, end in routes:
        if camera < start:
            camera = end
            answer += 1
    return answer