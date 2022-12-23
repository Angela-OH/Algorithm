import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, l, k = map(int, input().split())
    star = []
    max = 0

    for i in range(k):
        x, y = map(int, input().split())
        star.append((x, y))
    

    for i in range(k):
        for j in range(k):
            x, y = star[i][0], star[j][1]
            cnt = 0
            for u in range(k):
                if x <= star[u][0] <= x + l and y <= star[u][1] <= y + l:
                    cnt += 1
            if cnt > max:
                max = cnt
    
    print(k - max)