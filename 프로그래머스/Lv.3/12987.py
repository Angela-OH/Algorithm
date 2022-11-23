def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_index, b_index = 0, 0
    while b_index < len(B):
        if A[a_index] < B[b_index]:
            answer += 1
            a_index += 1
            b_index += 1
        else:
            b_index += 1
    return answer