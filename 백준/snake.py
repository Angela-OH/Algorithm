import queue
q = queue.Queue()

n = int(input())
k = int(input())

# 벽은 -1, 비어 있으면 0, 사과가 있으면 1, 뱀이 있으면 2
board = [[0 for _ in range(n+2)] for row in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        if i == 0 or i == n+1:
            board[i][j] = -1
        elif j == 0 or j == n+1:
            board[i][j] = -1

# 사과가 있는 칸 입력 받기
for _ in range(k):
    a, b = input().split()
    board[int(a)][int(b)] = 1

# 방향 변환 정보 입력 받기
l = int(input())
info = {}
for _ in range(l):
    x, c = input().split()
    info[int(x)] = c

direction = 0 # 이동 방향
second = 0 # 시간
# 뱀의 초기값 설정
x = 1
y = 1
board[x][y] = 2
q.put([x, y])

def check(): # 이동한 칸 check
    global x
    global y
    if board[x][y] == -1: # 이동한 칸에 벽
        return 0
    elif board[x][y] == 2: # 이동한 칸에 뱀
        return 0
    elif board[x][y] == 1: # 이동한 칸에 사과
        return 1
    return 2 # 이동할 칸이 비어있음

def move(): # 이동하기
    global x
    global y
    if direction == 0: # 오른쪽으로
        y += 1
    elif direction == 1: # 아래쪽으로
        x += 1
    elif direction == 2: # 왼쪽으로
        y -= 1
    else: # 위쪽으로
        x -= 1

def tail(): # 꼬리 비우기
    global q
    last = q.get()
    board[last[0]][last[1]] = 0

def change(): # 방향 바꾸기
    global second
    global direction
    direction_list = [
        [3, 1], 
        [0, 2], [1, 3], [2, 0]
    ] # [왼, 오]
    if info[second] == 'L': # 왼쪽
        direction = direction_list[direction][0]
    else: # 오른쪽
        direction = direction_list[direction][1]

while 1:
    move()
    q.put([x, y])
    second += 1
    checked = check()
    if checked == 0: # 종료 조건
        break
    elif checked == 2: # empty
        tail() 
    board[x][y] = 2
    if second in info:
        change()
print(second)