def isPrime(num):
    prime = []

    for i in range(2, num + 1):
        result = 0
        for j in range(2, i):
            if i % j == 0:
                result = 1
        if result == 0:
            prime.append(i)
    return prime

def solution(arr):
    answer = 1
    primes = isPrime(max(arr))
    
    rnd, index = 0, 0
    while index <= len(primes) - 1:
        prime = primes[index]
        cnt = 0
        rnd += 1
        for a in arr:
            if a / prime != int(a / prime):
                cnt += 1
        if (rnd == 1 and cnt == 0) or (rnd > 1 and len(arr) - cnt >= 2):
            for i in range(len(arr)):
                if arr[i] / prime == int(arr[i] / prime):
                    arr[i] = arr[i] // prime
            answer *= prime
            index = 0
            continue
        index += 1
                
    for a in arr:
        answer *= a
        
    return answer