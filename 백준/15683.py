import copy

min = 8 * 8

def count(array, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                count += 1
    return count

def horizontal(array, x, start, end, gap):
    temp = copy.deepcopy(array)
    for i in range(start, end, gap):
        if temp[x][i] == 0:
            temp[x][i] = -1
        elif temp[x][i] == 6:
            break
    return temp

def vertical(array, y, start, end, gap):
    temp = copy.deepcopy(array)
    for i in range(start, end, gap):
        if temp[i][y] == 0:
            temp[i][y] = -1
        elif temp[i][y] == 6:
            break
    return temp

def dfs(array, level):
    global min
    if level == len(cctv):
        cnt = count(array, n, m)
        if cnt < min:
            min = cnt
        return
    x, y = cctv[level]
    if array[x][y] == 1:
        dfs(horizontal(array, x, y - 1, -1, -1), level + 1)
        dfs(horizontal(array, x, y + 1, m, 1), level + 1)
        dfs(vertical(array, y, x - 1, -1, -1), level + 1)
        dfs(vertical(array, y, x + 1, n, 1), level + 1)
    elif array[x][y] == 2:
        dfs(horizontal(horizontal(array, x, y - 1, -1, -1), x, y + 1, m, 1), level + 1)
        dfs(vertical(vertical(array, y, x - 1, -1, -1), y, x + 1, n, 1), level + 1)
    elif array[x][y] == 3:
        dfs(horizontal(vertical(array, y, x - 1, -1, -1), x, y + 1, m, 1), level + 1)
        dfs(horizontal(vertical(array, y, x + 1, n, 1), x, y + 1, m, 1),level + 1)
        dfs(horizontal(vertical(array, y, x + 1, n, 1), x, y - 1, -1, -1), level + 1)
        dfs(horizontal(vertical(array, y, x - 1, -1, -1), x, y - 1, -1, -1), level + 1)
    elif array[x][y] == 4:
        hori = horizontal(horizontal(array, x, y - 1, -1, -1), x, y + 1, m, 1)
        verti = vertical(vertical(array, y, x - 1, -1, -1), y, x + 1, n, 1)
        dfs(vertical(hori, y, x - 1, -1, -1), level + 1)
        dfs(horizontal(verti, x, y + 1, m, 1), level + 1)
        dfs(vertical(hori, y, x + 1, n, 1), level + 1)
        dfs(horizontal(verti, x, y - 1, -1, -1), level + 1)
    elif array[x][y] == 5:
        hori = horizontal(horizontal(array, x, y - 1, -1, -1), x, y + 1, m, 1)
        verti = vertical(vertical(hori, y, x - 1, -1, -1), y, x + 1, n, 1)
        dfs(verti, level + 1)
        
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
#[[] for _ in range(8)]

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append((i, j))
dfs(arr, 0)
print(min)
