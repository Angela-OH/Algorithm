import sys

sys.setrecursionlimit(100000)
max = 0

def calculate(k, dungeons, result):
    cnt = 0
    for r in result:
        if k >= dungeons[r][0]:
            k -= dungeons[r][1]
            cnt += 1
    return cnt

def permutation(k, dungeons, n, index, visited, result):
    global max
    if index == n:
        cnt = calculate(k, dungeons, result)
        if cnt > max:
            max = cnt
        return

    for i in range(n):
        if visited[i] != 0:
            continue

        result.append(i)
        visited[i] = 1

        permutation(k, dungeons, n, index + 1, visited, result)

        visited[result.pop()] = 0


def solution(k, dungeons):
    visited = [0 for _ in range(len(dungeons))]
    result = permutation(k, dungeons, len(dungeons), 0, visited, [])
    print(result)
    return max