def solution(elements):
    n = len(elements)
    sum_element = set([])
    for i in range(0, n): # 연속 부분 수열의 길이
        for j in range(n): # 시작점
            start = j
            end = (j + i) % n
            if start > end:
                sum_element.add(sum(elements[start:] + elements[:end + 1]))
            else:
                sum_element.add(sum(elements[start: end + 1]))
    return len(sum_element)