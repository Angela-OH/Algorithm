import sys
input = sys.stdin.readline
INF = sys.maxsize

m, n, l = map(int, input().split())
dp = [0 for _ in range(m)]
loc = [0]
loc.extend(list(map(int, input().split())))
loc.sort() # x 좌표 기준으로 정렬
loc.append(INF)
animal = []

for i in range(n):
    a, b = map(int, input().split())
    if b > l:
        continue
    animal.append((a, b))
animal.sort() # a를 기준으로 정렬

animal_idx = 0
cnt = 0
left, right = 0, 1 # 구간 시작, 끝
while left <= m and animal_idx < len(animal):
    x, y = animal[animal_idx]
    if x > loc[right]: # 현재 구간을 벗어남
        left = right # 다음 구간 탐색 시작
        right += 1
        continue
    if (left != 0 and abs(x - loc[left]) + y <= l) or abs(x - loc[right]) + y <= l:
        cnt += 1
    animal_idx += 1
    
print(cnt)