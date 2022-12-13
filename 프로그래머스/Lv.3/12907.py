def solution(n, money):
    money.sort()
    info = [0 for _ in range(n + 1)]
    info[0] = 1
    
    for i in range(len(money)): 
        for j in range(1, n + 1):
            if j - money[i] < 0:
                continue
            info[j] += info[j - money[i]]
    return info[n] % 1000000007