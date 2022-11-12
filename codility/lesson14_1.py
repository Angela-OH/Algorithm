# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def valid(A, K, max_size):
    sum, cnt = 0, 0
    for a in A:
        if sum + a > max_size:
            sum = a
            cnt += 1
            if cnt >= K:
                return False
        else:
            sum += a

    return True

def solution(K, M, A):
    # write your code in Python 3.8.10
    lower_bound = max(A) # if k > len(A)
    upper_bound = sum(A) # if k == 1

    if K > len(A):
        return lower_bound
    elif K == 1:
        return upper_bound
    
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if valid(A, K, mid): # Can I seperate A into K blocks with max size mid?
            upper_bound = mid - 1 # Yes, try lower max size
        else:
            lower_bound = mid + 1 # No, make max size bigger then
    return lower_bound