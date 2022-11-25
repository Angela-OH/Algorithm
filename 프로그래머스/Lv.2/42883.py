def find(arr):
    max = '0'
    index = 0
    for i, w in enumerate(arr):
        if w > max:
            max = w
            index = i
        if w == '9':
            break
    return (index, max)

def solution(number, k):
    n = len(number)
    k = n - k
    cnt, index = 0, 0
    answer = ''
    
    while cnt < k:
        left = k - cnt
        result = find(number[index: n - left + 1])
        index = index + result[0] + 1
        answer += result[1]
        cnt += 1
        
    return answer