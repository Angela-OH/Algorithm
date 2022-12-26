def isPromising(level, x): # level은 행, x는 열을 의미
    for i in range(level):
        # 다른 행에서 선택한 열을 선택할 수 없음 (수직선상 존재)
        # 다른 행에서 선택한 열 대각선 상 존재할 수 없음
        if chess[i] == x or abs(i - level) == abs(chess[i] - x):
            return False
 
    return True

def dfs(level): # level은 행을 의미
    global answer
    if level == n:
        answer += 1
        return
    for i in range(n):
        if isPromising(level, i):
            chess[level] = i
            dfs(level + 1)


n = int(input())
chess = [0 for _ in range(n)] # 인덱스는 행, 배열값은 열을 의미
answer = 0

dfs(0)

print(answer)