# 최소 신장 트리를 만들기 위해 크루스칼 알고리즘 구현 
import sys
import heapq
input = sys.stdin.readline

def find(parent, index):
    if index != parent[index]:
        parent[index] = find(parent, parent[index]) # root까지 찾기
    return parent[index]

def union(parent, i, j):
    root1 = find(parent, i)
    root2 = find(parent, j)
    parent[root1] = root2

def main():
    n, c = map(int, input().split())
    parent = [i for i in range(n)]
    loc = [[0, 0] for _ in range(n)]
    info = []
    count = 0
    answer = 0

    for i in range(n):
        x, y = map(int, input().split())
        loc[i][0] = x
        loc[i][1] = y

    for i in range(n):
        for j in range(i + 1, n):
            distance = pow((loc[i][0] - loc[j][0]), 2) + pow((loc[i][1] - loc[j][1]), 2)
            if distance >= c:
                heapq.heappush(info, (distance, i, j))

    while count < n - 1:
        if not info:
            answer = -1
            break
        distance, i, j = heapq.heappop(info)
        if find(parent, i) != find(parent, j):
            union(parent, i, j)
            count += 1
            answer += distance

    print(answer)

main()