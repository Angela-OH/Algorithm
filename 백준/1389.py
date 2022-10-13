import sys

def cabin_bacon(n, friends):
    connect = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    cb = []

    for i in range(1, n + 1):
        queue = [i]
        connect[i][i] = 0
        sum = 0

        while queue:
            node = queue.pop(0)
            for friend in friends[node]:
                if connect[i][friend] == -1: # not visited yet
                    connect[i][friend] = connect[i][node] + 1 
                    queue.append(friend)            
        
        for j in range(1, n + 1):
            sum += connect[i][j]
        
        cb.append((i, sum))

    cb.sort(key = lambda x: x[1])

    return cb[0][0]

if __name__ == "__main__":
    n, m = map(int, input().split())
    friends = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        friends[a].append(b)
        friends[b].append(a)

    print(cabin_bacon(n, friends))
