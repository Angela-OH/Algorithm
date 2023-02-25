def change(n, k): # n을 k진수로 변환
    res = ''
    
    while n >= k:
        res += str(n % k)
        n = n // k
    res += str(n)
    
    return res[::-1]

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = change(n, k).split('0')
    
    for n in num:
        if not n: 
            continue
        if isPrime(int(n)):
            answer += 1
            
    return answer
            