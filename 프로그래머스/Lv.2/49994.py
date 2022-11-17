def solution(dirs):
    answer = 0
    x_visited = [[[0 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    y_visited = [[[0 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    current = (5, 5)
    
    for dir in dirs:
        isX = 0
        if dir == 'U':
            x, y = current[0] - 1, current[1]
            isX = 1
        elif dir == 'L':
            x, y = current[0], current[1] - 1
        elif dir == 'R':
            x, y = current[0], current[1] + 1
        else:
            x, y = current[0] + 1, current[1]
            isX = 1
        if 0 <= x <= 10 and 0 <= y <= 10:
            if isX == 1: # 위, 아래 이동
                if x_visited[y][current[0]][x] == 0:
                    x_visited[y][current[0]][x] = 1
                    x_visited[y][x][current[0]] = 1
                    answer += 1
            else:
                if y_visited[x][current[1]][y] == 0:
                    y_visited[x][current[1]][y] = 1
                    y_visited[x][y][current[1]] = 1
                    answer += 1
            current = (x, y)
    return answer