arr_list = []
def permutation(n, k, numbers):
    used = [0 for _ in range(n)]
    def generate(chosen, used):
        if len(chosen) == k:
            if chosen not in arr_list and chosen[0] != '0':
                arr_list.append(chosen[:])
            return
        for i in range(n):
            if used[i] == 0:
                chosen.append(numbers[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        permutation(len(numbers), i, numbers)
    
    for i in arr_list:
        s = ''
        for j in i:
            s += j
        if isPrime(int(s)):
            answer += 1

    return answer