def solution(n):
    answer = 0
    f = [0 for _ in range(100001)]
    f[0], f[1] = 0, 1
    for i in range(2, n + 1):
        f[i] = f[i - 2] + f[i - 1]
    answer = f[n] % 1234567
    return answer