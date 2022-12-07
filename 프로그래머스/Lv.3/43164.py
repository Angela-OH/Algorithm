import sys
sys.setrecursionlimit(10**6)

answer_list = []

def route(index, tickets, visited, answer, count):
    start, dest = tickets[index][0], tickets[index][1]
    answer[count] = dest
    if count == len(answer) - 1:
        answer_list.append(answer[:])
        return
    for i, t in enumerate(tickets):
        if t[0] == dest and visited[i] == 0:
            visited[i] = 1
            route(i, tickets, visited, answer, count + 1)
            visited[i] = 0

def solution(tickets):
    tickets.sort()
    for i, t in enumerate(tickets):
        if t[0] == 'ICN':
            answer = [0 for _ in range(len(tickets) + 1)]
            answer[0] = 'ICN'
            visited = [0 for _ in range(len(tickets))]
            visited[i] = 1
            answer = route(i, tickets, visited, answer, 1)
    return answer_list[0]