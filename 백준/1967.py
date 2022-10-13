import sys

def dfs(tree, start):
    max = 0
    global end

    stack.append([start, 0])
    visited[start] = 1
    
    while stack:
        pop_node, dist = stack.pop()
        for next_node in tree[pop_node]:
            if visited[next_node[0]] == 0:
                visited[next_node[0]] = 1
                new_dist = dist + next_node[1]
                stack.append([next_node[0], new_dist])
                if new_dist > max:
                    max = new_dist
                    end = next_node[0]

    return max

n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
stack = []
end = 0
for i in range(n - 1):
    text = list(map(int, sys.stdin.readline().split()))
    tree[text[0]].append((text[1], text[2]))
    tree[text[1]].append((text[0], text[2]))

dfs(tree, 1)

for i in range(len(visited)):
    visited[i] = 0
    
print(dfs(tree, end))