def move(location, horse, x, y, new_x, new_y):
    for index in location[x][y]:
        horse[index][0] = new_x
        horse[index][1] = new_y
def main():
    n, k = map(int, input().split())
    info = [[] for _ in range(n + 2)]
    info[0].extend([2 for _ in range(n + 2)])
    info[n + 1].extend([2 for _ in range(n + 2)])
    horse = [[] for _ in range(k)]
    location = [[[] for _ in range(n + 2)] for _ in range(n + 2)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    reverse_direction = {1: 2, 2: 1, 3: 4, 4: 3}
    turn = 0

    for i in range(n):
        info[i + 1].append(2)
        info[i + 1].extend(list(map(int, input().split())))
        info[i + 1].append(2)

    for i in range(k):
        horse[i].extend(list(map(int, input().split())))
        location[horse[i][0]][horse[i][1]].append(i)

    while turn <= 1000:
        turn += 1
        for i in range(k):
            x, y, direction = horse[i][0], horse[i][1], horse[i][2]
            if location[x][y][0] != i: # 맨 아래 말이 아니면 움직일 수 x
                continue
        
            checked = 0 # 파란색일 경우를 위해
            while checked != 1:
                new_x, new_y = x + dx[direction - 1], y + dy[direction - 1]
                if info[new_x][new_y] == 0:
                    move(location, horse, x, y, new_x, new_y)
                    move_horse = location[x][y]
                    checked = 1
                elif info[new_x][new_y] == 1:
                    move(location, horse, x, y, new_x, new_y)
                    move_horse = location[x][y][::-1]
                    checked = 1
                else:
                    if checked == 0:
                        direction = reverse_direction[direction]
                        horse[i][2] = direction
                        checked = -1
                        continue
                    else: # 파란색 갔다가 파란색에 다시 온 경우
                        checked = 1
                        continue
                location[new_x][new_y].extend(move_horse)
                if len(location[new_x][new_y]) == 4:
                    return turn
                location[x][y] = []
    return -1

print(main())
