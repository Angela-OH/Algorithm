def move(ans):
    for a in range(12 * 6):
        if ans[a] == 0:
            break
        arr[ans[a][0]][ans[a][1]] = '.'
        for i in range(ans[a][0] - 1, -1, -1):
            if arr[i][ans[a][1]] != '.':
                arr[i + 1][ans[a][1]] = arr[i][ans[a][1]]
                arr[i][ans[a][1]] = '.'

def dfs(start, visited):
    stack = []
    ans = [0 for _ in range(12 * 6)]
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

    x, y = start
    stack.append((x, y, arr[x][y]))
    visited[x][y] = 1
    ans[0] = start
    ans_index = 1

    while stack:
        x, y, alpha = stack.pop()

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < 12 and 0 <= new_y < 6:
                if arr[new_x][new_y] == alpha and visited[new_x][new_y] == 0:
                    stack.append((new_x, new_y, arr[new_x][new_y]))
                    visited[new_x][new_y] = 1
                    ans[ans_index] = (new_x, new_y)
                    ans_index += 1

    if ans_index >= 4:
        return ans
    return []

def puyo():
    burst = 0

    while True:
        visited = [[0 for _ in range(6)] for _ in range(12)]
        result = []
        for i in range(12):
            for j in range(6):
                if arr[i][j] != '.':
                    if visited[i][j] == 0:
                        dfs_result = dfs((i, j), visited)
                        if dfs_result:
                            result.append(dfs_result)
                
        if result:
            burst += 1
            for r in result:
                move(r)
        else:
            return burst

arr = [list(input()) for _ in range(12)]

print(puyo())