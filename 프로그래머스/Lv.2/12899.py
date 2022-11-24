def solution(n):
    num = ['1', '2', '4']
    if n == 1:
        return num[0]
    s = ''
    while n > 0:
        quotient = (n - 1) // 3
        remainer = (n - 1) % 3
        s = num[remainer] + s
        n = quotient
        
    return s