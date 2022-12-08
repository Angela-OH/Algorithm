def check(place, i, j):
    dx, dy = [0, 1, -1], [1, 0, 0]
    move = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (-1, 0), (-1, 1), (-2, 0)]
    move = [(i + a, j + b) for a, b in move]
    queue = [(i, j)]
    visited = [0 for _ in range(len(move))]
    visited[0] = 1
    while queue:
        x, y = queue.pop()
        for k in range(len(dx)):
            new_x, new_y = x + dx[k], y + dy[k]
            if 0 <= new_x < len(place) and 0 <= new_y < len(place[0]):
                if (new_x == i and new_y == j) or (new_x, new_y) not in move:
                    continue
                index = move.index((new_x, new_y))
                if place[new_x][new_y] == 'O' and visited[index] == 0:
                    queue.append((new_x, new_y))
                    visited[index] = 1
                if place[new_x][new_y] == 'P':
                    print((i, j, new_x, new_y))
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        result = 1
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    if not check(place, i, j):
                        result = 0
        answer.append(result)
    return answer