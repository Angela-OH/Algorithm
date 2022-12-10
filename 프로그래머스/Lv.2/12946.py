import sys
sys.setrecursionlimit(10**6)

answer = []

def hanoi(n, start, end, additional):
    if n == 1:
        answer.append([start, end])
        return
    hanoi(n - 1, start, additional, end)
    answer.append([start, end])
    hanoi(n - 1, additional, end, start)
    
def solution(n):
    hanoi(n, 1, 3, 2)
    return answer