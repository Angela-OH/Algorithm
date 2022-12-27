import sys
import heapq
input = sys.stdin.readline

n = int(input())
info = [[] for _ in range(n)]
ball_color = {} # 같은 색깔의 볼 정보
sum = [0 for _ in range(n)]
answer = [0 for _ in range(n)]

for i in range(n):
    color, size = map(int, input().split())
    info[i] = [size, color, i]
    if color not in ball_color:
        ball_color[color] = 0

info.sort(key = lambda x: (x[0], x[1], x[2]))

sum = 0
j = 0
for i in range(n):
    # while 문 안에 들어가지 못하면 누적합 증가 x
    while info[j][0] < info[i][0]:
        sum += info[j][0]
        ball_color[info[j][1]] += info[j][0]
        j += 1
    answer[info[i][2]] = sum - ball_color[info[i][1]]

for i in range(n):
    print(answer[i])