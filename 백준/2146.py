from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def init(n, visited):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def dfs(n, info, visited, i, j, color):
    info[i][j] = color
    stack = [(i, j)]
    visited[i][j] = True
    
    while stack:
        i, j = stack.pop()
        for k in range(4):
            new_i, new_j = i + dx[k], j + dy[k]
            if 0 <= new_i < n and 0 <= new_j < n:
                if info[new_i][new_j] != 0 and not visited[new_i][new_j]:
                    stack.append((new_i, new_j))
                    visited[new_i][new_j] = True
                    info[new_i][new_j] = color

def bfs(n, info, visited, i, j):
    color = info[i][j]
    queue = deque([])
    queue.append((i, j, 0))
    visited[i][j] = True

    while queue:
        i, j, count = queue.popleft()
        for k in range(4):
            new_i, new_j = i + dx[k], j + dy[k]
            if 0 <= new_i < n and 0 <= new_j < n:
                if info[new_i][new_j] == color:
                    continue
                if info[new_i][new_j] != 0:
                    return count
                elif not visited[new_i][new_j]:
                    queue.append((new_i, new_j, count + 1))
                    visited[new_i][new_j] = True

    return count

if __name__ == "__main__":
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    color = 1
    answer = 100 * 100

    # 섬 구분짓기
    for i in range(n):
        for j in range(n):
            if info[i][j] != 0 and not visited[i][j]:
                dfs(n, info, visited, i, j, color)
                color += 1

    # 최소 길이 다리 구하기
    for i in range(n):
        for j in range(n):
            if info[i][j] != 0:
                init(n, visited)
                count = bfs(n, info, visited, i, j)
                if count != 0 and count < answer:
                    answer = count

    print(answer)