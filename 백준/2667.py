import sys

def check(n, maps):
    index = ()
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                index = (i, j)
                return index
    return index

def dfs(n, maps):
    stack = []
    apartment = []
    move = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    ]
    
    while True:
        index = check(n, maps)
        if not index:
            break
        stack.append(index)
        maps[index[0]][index[1]] = -1 # visited
        cnt = 1

        while stack:
            node = stack.pop()
            x, y = node[0], node[1]
            for i in range(len(move)):
                a = x + move[i][0]
                b = y + move[i][1]
                if (0 <= a < n) and (0 <= b < n):
                    if maps[a][b] == 1:
                        stack.append((a, b))
                        maps[a][b] = -1
                        cnt += 1


        apartment.append(cnt)
    
    apartment.sort()
    apart_len = len(apartment)
    print(apart_len)
    for i in range(apart_len):
        print(apartment[i])

if __name__ == "__main__":
    n = int(input())
    maps = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        inputs = input()
        for j in range(n):
            maps[i][j] = int(inputs[j])

    dfs(n, maps)

