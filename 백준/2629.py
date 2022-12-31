def isChoose(depth, left, right):

    if depth == n: # 종료조건
        answer[abs(left-right)] = True
        return
    
    if not visited[depth][abs(left-right)]:
        isChoose(depth + 1, left, right) # 추를 안 올림
        isChoose(depth + 1, left + ball[depth], right) # 추를 왼쪽에 올림
        isChoose(depth + 1, left, right + ball[depth]) # 추를 오른쪽에 올림
        visited[depth][abs(left-right)] = True

n = int(input())
ball = list(map(int, input().split()))
answer = [False for _ in range(40001)]
visited = [[False for _ in range(15001)] for _ in range(n)]

isChoose(0, 0, 0)

t = int(input())
case = list(map(int, input().split()))
for i in range(t):
    if answer[case[i]]:
        print('Y', end = ' ')
    else:
        print('N', end = ' ')