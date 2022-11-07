def binary_search_asc(arr, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

def binary_search_desc(arr, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            start = mid + 1
        else:
            end = mid
    return end

def solution(kyul):
    # 최장증가수열 + 이진탐색으로 풀기 (효율성..)
    answer = 0
    asc, desc = [], []
    asc.append(kyul[0])
    desc.append(kyul[0])

    # 오름차순 확인
    index = 1
    while index < len(kyul):
        if asc[-1] < kyul[index]:
            asc.append(kyul[index])
        else:
            asc[binary_search_asc(asc, 0, len(asc) - 1, kyul[index])] = kyul[index]
        index += 1
    
    # 내림차순 확인
    index = 1
    while index < len(kyul):
        if desc[-1] > kyul[index]:
            desc.append(kyul[index])
        else:
            desc[binary_search_desc(desc, 0, len(desc) - 1, kyul[index])] = kyul[index]
        index += 1
    
    if len(asc) > len(desc):
        answer = len(kyul) - len(asc)
    else:
        answer = len(kyul) - len(desc)

    return answer

'''
ex1 = [12, 14, 13, 19]
ex2 = [1, 3, 5, 4, 2]
ex3 = [a for a in range(100000)]
ex3[2] = 1
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
'''