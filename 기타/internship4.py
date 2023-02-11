def check(visited):
    for v in visited:
        if v == 0:
            return True
    return False
    
def find_job(jobs, visited, time, code):
    next_job = {}
    max, max_code = 0, 101

    for i in range(len(jobs)):
        if visited[i] != 0: # 완료된 작업
            continue

        if jobs[i][0] <= time:
            if jobs[i][2] not in next_job:
                next_job[jobs[i][2]] = [i]
            else:
                next_job[jobs[i][2]].append(i)

    if not next_job: # 현재 작업할 수 있는 거 x
        return (-1, -1)

    if code in next_job: # 분류코드가 이전과 동일한 거
        return (code, next_job[code]) 
    else: # 중요도 높은 순 + 분류코드 낮은 순
        for next_code in next_job:
            sum = 0 # 중요도의 합
            for i in next_job[next_code]:
                sum += jobs[i][3]
            if sum >= max:
                if sum > max:
                    max = sum
                    max_code = next_code
                elif next_code < max_code:
                    max_code = next_code
        return (max_code, next_job[max_code]) 

def solution(jobs):
    time, code = jobs[0][0] + jobs[0][1], jobs[0][2] # 1번 작업이 제일 먼저 실행됨
    answer = [code]
    visited = [0 for _ in range(len(jobs))] # 처리된 작업 여부
    visited[0] = 1

    while check(visited):
        code, next_jobs = find_job(jobs, visited, time, code)
        if code == -1 and next_jobs == -1:
            time += 1
            continue
        if answer[-1] != code:
            answer.append(code)
        sum = 0
        for next in next_jobs: # 걸리는 시간 계산
            sum += jobs[next][1]
            visited[next] = 1
        time += sum

    return answer