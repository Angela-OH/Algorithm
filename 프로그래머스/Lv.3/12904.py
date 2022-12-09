def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        start, end = i, n - 1
        tmp_end = end
        check = 0
        count = 0
        while start <= end:
            if start == end:
                count += 1
                break
            
            if s[start] == s[end]:
                start += 1
                if check == 0:
                    tmp_end = end
                    check += 1
                end -= 1
                count += 2
            else:
                if count > 0:
                    count = 0
                    check = 0
                    start = i
                    end = tmp_end
                end -= 1
                
        if count > answer:
            answer = count
            
    return answer