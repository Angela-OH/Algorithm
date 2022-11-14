def solution(phone_book):
    answer = True
    dic = {}
    for phone in phone_book:
        dic[phone] = 1
        
    for phone in phone_book:
        tmp = ''
        for p in phone:
            tmp += p
            if tmp in dic and tmp != phone:
                return False
                
    return answer