def solution(s):
    count, zero_count = 0, 0
    
    while s != '1':
        zero = s.count('0')
        zero_count += zero
        count += 1
        s = format(len(s) - zero, 'b')
       
    answer = [count, zero_count]
    
    return answer