# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    num = {}
    for i in range(len(A)):
        if A[i] in num:
            num[A[i]] += 1
        else:
            num[A[i]] = 1

    for elemt in num:
        if num[elemt] % 2 != 0:
            return elemt