def find_curve(d, g):
    curve_list = [d]
    level = 0
    while level < g:
        for i in range(len(curve_list) - 1, -1, -1):
            curve_list.append((curve_list[i] + 1) % 4)
        level += 1
    return curve_list

def dragon(x, y, d, g):
    curve_list = find_curve(d, g)
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    for curve in curve_list:
        new_x, new_y = x + dx[curve], y + dy[curve]
        arr[new_x][new_y] = 1
        x, y = new_x, new_y
   
n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1
    dragon(x, y, d, g)

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            if arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
                cnt += 1

print(cnt)