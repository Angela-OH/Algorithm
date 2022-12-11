def rotate(n, key):
    new_key = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[j][abs(i + 1 - n)] = key[i][j]
    return new_key

def check(n, key, m, info, count):                
    for i in range(m + n - 1):
        for j in range(m + n - 1):
            count_cpy = count
            isFalse = 0
            for a in range(n):
                for b in range(n):
                    if key[a][b] == info[i + a][j + b]:
                        isFalse = 1
                    if key[a][b] == 1 and info[i + a][j + b] == 0:
                        count_cpy -= 1
            if count_cpy == 0 and isFalse == 0:
                return True
    return False

def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)
    info = [[-1 for _ in range(m + 2 * (n - 1))] for _ in range(m + 2 * (n - 1))]
    count = 0 # 홈의 개수
    for i in range(m):
        for j in range(m):
            info[i + n - 1][j + n - 1] = lock[i][j]
            if lock[i][j] == 0:
                count += 1
    
    for k in range(4): # 90, 180, 270, 360(0) 회전
        key = rotate(n, key)
        if check(n, key, m, info, count):
            return True
    return answer