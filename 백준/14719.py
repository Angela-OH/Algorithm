def rain():
    count = 0
    for i in range(h):
        last_block = -1
        for j in range(w):
            if block[i][j] == 1:
                if last_block == -1:
                    last_block = j
                else:
                    count += (j - last_block - 1)
                    last_block = j
    return count

h, w = map(int, input().split())
block = [[0 for _ in range(w + 1)] for _ in range(h)]
info = list(map(int, input().split()))

for i in range(w):
    for j in range(info[i]):
        block[j][i] = 1

print(rain())
