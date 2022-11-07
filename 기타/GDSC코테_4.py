def change(current, server):
    for i in range(len(server)):
        if server[i]:
            t = server[i][0][0]
        j = 0
        while j < len(server[i]):
            if t < server[i][j][0]:
                t = server[i][j][0]
            if (t + server[i][j][1]) <= current:
                t += server[i][j][1]
                del server[i][j]
                continue
            else:
                break
            j += 1
            
    return server

def time_count(current, server):
    max = 0
    for s in server: # 걸리는 시간 계산
        index, time = 0, current
        while index < len(s):
            if time < s[index][0]:
                time = s[index][0]
                continue
            time += s[index][1]
            index += 1
        if time > max:
            max = time
    return max

def least_connection(numServer, logs):
    time = 0
    server = [[] for _ in range(numServer)]
    for current, duration in logs:
        change(current, server) # 서버 상황 업데이트

        cnt, index = len(logs), -1 # 어디에 요청을 보낼지
        for i in range(len(server)):
            if len(server[i]) < cnt:
                cnt = len(server[i])
                index = i
    
        server[index].append((current, duration))
        time = current
    
    return time_count(time, server)

def round_robin(numServer, logs):
    cnt = 0
    server = [[] for _ in range(numServer)]
    for log in logs: # 어디에 요청을 보낼지
        server[cnt % numServer].append(log)
        cnt += 1
    
    return time_count(0, server) # 걸리는 시간 계산

def solution(numServer, logs):
    first = round_robin(numServer, logs)
    second = least_connection(numServer, logs)
    
    if first == second:
        answer = [0, 0]
    elif first < second:
        answer = [1, second - first]
    else:
        answer = [2, first - second]

    return answer

ex1 = [[1, 4], [2, 5], [3, 1], [4, 6], [8, 2], [10, 4]]
ex2 = [[1, 4], [2, 5], [3, 1], [4, 7], [8, 1], [15, 16]]
print(solution(2, ex1))
print(solution(3, ex2))