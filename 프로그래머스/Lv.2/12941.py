def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse = 1)
    for i in range(len(A)):
        answer += A[i] * B[i]
        
    return answer