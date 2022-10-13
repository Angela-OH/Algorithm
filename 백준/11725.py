import sys

def bfs(n, tree, start):
    queue = [start]
    root = [0 for i in range(n + 1)]

    while queue:
        node = queue.pop(0)
        for i in tree[node]:
            if root[i] == 0: # not visited yet
                queue.append(i)
                root[i] = node

    return root

if __name__ == "__main__":
    n = int(input())
    tree = [[] for i in range(n + 1)]

    for i in range(n - 1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        tree[a].append(b)
        tree[b].append(a)
    
    root = bfs(n, tree, 1)
    
    for i in range(2, len(root)):
        print(root[i])