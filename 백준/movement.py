from collections import deque
n, l, r = map(int, input().split())
popularity = [list(map(int, input().split())) for _ in range(n)]
day = 0
graph = dict()

def check(value, input, x, y): # 인구 이동 조건 확인
    if (input >= l) and (input <= r):
        value.append((x, y))

def border(i, j): 
    value = []
    if i-1 >= 0:
        top = abs(popularity[i-1][j]-popularity[i][j])      
        check(value, top, i-1, j)
    if i+1 < n:
        bottom = abs(popularity[i+1][j]-popularity[i][j])
        check(value, bottom, i+1, j)
    if j-1 >= 0:
        left = abs(popularity[i][j-1]-popularity[i][j])
        check(value, left, i, j-1)
    if j+1 < n:
        right = abs(popularity[i][j+1]-popularity[i][j])
        check(value, right, i, j+1)
    if value:
        graph[(i, j)] = value

def bfs(start): 
    visit = list()
    queue = deque()
    queue.append(start)
    while queue:
        enqueue = queue.popleft()
        if enqueue not in visit:
            visit.append(enqueue)
            queue.extend(graph[enqueue])
    return visit

while True:
    # 인접 그래프 그리기
    for i in range(n):
        for j in range(n):
            border(i, j)

    # 종료 조건
    if not graph: 
        break

    while graph:
        movement = bfs(list(graph.keys())[0])
        sum = 0
        # 연합 인구수 조정
        for move in movement:
            sum += popularity[move[0]][move[1]]
        result = int(sum/len(movement))
        for move in movement:
            popularity[move[0]][move[1]] = result
            del(graph[move])
    day += 1

print(day)