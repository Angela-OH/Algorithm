# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.8.10
    length = len(A)
    if length:
        K %= length
    return A[(-1 * K):] + A[:(-1 * K)]

print(solution([3, 8, 9, 7, 6], 3))
print(solution([], 5))