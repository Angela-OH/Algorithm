def bfs(a, b):
    level = {a: 0}
    queue = [a]

    while queue:
        node = queue.pop(0)
        new = [node * 2, node * 10 + 1]
        for i in new:
            if i < b and i not in level:
                level[i] = level[node] + 1
                queue.append(i)
            if i == b:
                return level[node] + 2
    return -1

if __name__ == "__main__":
    a, b = map(int, input().split())

    print(bfs(a, b))