def check(x, y):
    for i in range(x):
        if chess[i] == y or abs(x - i) == abs(y - chess[i]):
            return 0
    return 1

def dfs(x):
    global case

    if x == n:
        case += 1
        return

    for i in range(n):
        if check(x, i):
            chess[x] = i
            dfs(x + 1)


n = int(input())

chess = [0 for _ in range(n)]
case = 0

dfs(0)

print(case)
