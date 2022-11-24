def solution(n, stations, w):
    start = 1
    answer = 0
    while stations:
        station = stations.pop(0)
        end = station - w
        if start < end:
            count = end - start
            answer += count // (2 * w + 1)
            if count % (2 * w + 1) != 0:
                answer += 1
        start = station + w + 1
    
    if start <= n:
        count = n + 1 - start
        answer += count // (2 * w + 1)
        if count % (2 * w + 1) != 0:
            answer += 1
    
    return answer