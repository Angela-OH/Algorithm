def solution(n, s):
    answer = []
    if s % n == 0:
        answer = [(s/n) for _ in range(n)]
    else:
        if n > s:
            answer = [-1]
        else:
            answer = [(s//n) for _ in range(n)]
            left = s % n
            for i in range(len(answer) - 1, -1, -1):
                if left == 0:
                    break
                answer[i] += 1
                left -= 1
            
    return answer