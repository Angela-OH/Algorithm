from collections import deque

def change(current, server):
    for i in range(len(server)):
        if not server[i]:
            continue
        sum = server[i][0][0]
        while server[i]:
            sum += server[i][0][1]
            if sum <= current:
                server[i].popleft()
                if server[i] and server[i][0][0] < sum:
                    server[i][0][0] = sum
            else:
                break
            
    return server

def time_count(server):
    max = 0
    for s in server: # 걸리는 시간 계산
        if not s:
            continue
        time = s[0][0]
        for start, duration in s:
            if time < start:
                time = start
            time += duration
        if time > max:
            max = time

    return max

def least_connection(numServer, logs):
    server = [deque([]) for _ in range(numServer)]
    for current, duration in logs:
        server = change(current, server) # 서버 상황 업데이트

        cnt, index = len(logs), -1 # 어디에 요청을 보낼지
        for i in range(len(server)):
            if len(server[i]) < cnt:
                cnt = len(server[i])
                index = i
    
        server[index].append([current, duration])
    
    return time_count(server)

def round_robin(numServer, logs):
    cnt = 0
    server = [[] for _ in range(numServer)]
    for log in logs: # 어디에 요청을 보낼지
        server[cnt % numServer].append(log)
        cnt += 1
    
    return time_count(server) # 걸리는 시간 계산

def solution(numServer, logs):
    first = round_robin(numServer, logs)
    second = least_connection(numServer, logs)
    #print(first, second)
    if first == second:
        answer = [0, 0]
    elif first < second:
        answer = [1, second - first]
    else:
        answer = [2, first - second]

    return answer

ex1 = [[1, 4], [2, 5], [3, 1], [4, 6], [8, 2], [10, 4]]
ex2 = [[1, 4], [2, 5], [3, 1], [4, 7], [8, 2], [10, 14], [12, 20], [14, 2], [16, 15]]
#print(solution(2, ex1))
#print(solution(3, ex2))