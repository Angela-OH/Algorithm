from collections import deque

def bfs(x):
    queue = deque([])
    queue.append((x, [x]))
    visited = [False for _ in range(max(n, k) * 2)]
    visited[x] = True

    while queue:
        x, r = queue.popleft()
        for i in [x + 1, x - 1, x * 2]:
            if i < 0 or i >= 2 * max(k, n):
                continue
            if visited[i]:
                continue
            visited[i] = True
            new_r = r[:]
            new_r.append(i)
            if i == k:
                return new_r
            queue.append((i, new_r))


n, k = map(int, input().split())

if k <= n:
    print(n - k)
    for i in range(n, k - 1, -1):
        print(i, end = ' ')
    exit()

route = bfs(n)

print(len(route) - 1)
for r in route:
    print(r, end = ' ')