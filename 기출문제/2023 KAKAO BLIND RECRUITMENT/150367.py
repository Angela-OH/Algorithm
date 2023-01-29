import sys
sys.setrecursionlimit(10 ** 6)

def calculate(n): # 일치하는 or 근접하면서 큰 포화 트리 노드 개수 반환
    # cnt[i]: 높이 (i + 1) 일 때 포화 트리 노드 개수
    cnt = [1, 3, 7, 15, 31, 63] # 10**15를 이진수로 표현했을 때 길이: 50
    for c in cnt:
        if c >= n:
            return c

def to_bin(n):
    gap = calculate(len(n)) - len(n)
    n = '0' * gap + n
    return n

def determine(str, start, end): 
    stack = [(start, end)]
    while stack:
        s, e = stack.pop()
        if s >= e:
            continue
        n = (s + e) // 2
        if str[n] == '0':
            if str[(s + n - 1) // 2] != '0' or str[(n + 1 + e) // 2] != '0':
                return False
        
        stack.append((s, n - 1))
        stack.append((n + 1, e))

    return True

def solution(numbers):
    answer = []
    for n in numbers:
        bin_n = to_bin(bin(n)[2:]) # 앞에 0b 제거
        if determine(bin_n, 0, len(bin_n) - 1):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer