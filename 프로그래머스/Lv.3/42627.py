import heapq

def solution(jobs):
    answer, time, count = 0, 0, 0
    n = len(jobs)
    isDone = [0 for _ in range(n)]

    while count < n:
        heap = []
        for j in range(n):
            if jobs[j][0] <= time and isDone[j] == 0:
                heapq.heappush(heap, (jobs[j][1], jobs[j][0], j))
        if heap:
            duration, start, index = heapq.heappop(heap)
            answer += (time - start + duration)
            time += duration
            isDone[index] = 1
            count += 1
        else:
            time += 1
    return answer // n