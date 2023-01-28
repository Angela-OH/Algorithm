def bargain(m):
    b = []
    b_list = [0 for i in range(m)]
    b_type = [0.1, 0.2, 0.3, 0.4]
    stack = [(0.1, 0), (0.2, 0), (0.3, 0), (0.4, 0)]
    while stack:
        p, i = stack.pop()
        b_list[i] = p
        if i == m - 1:
            b.append(b_list[:])
            continue
        for t in b_type:
            stack.append((t, i + 1))

    return b
    
def solution(users, emoticons):
    max_user, max_value = 0, 0 # 플러스 가입자 수, 매출액
    
    for b in bargain(len(emoticons)):
        user, value = 0, 0
        for u in users:
            sum = 0
            for i in range(len(emoticons)):
                if b[i] < (u[0] / 100): continue
                sum += (emoticons[i] * (1 - b[i]))
            if sum >= u[1]:
                user += 1
            else: value += sum
        if user > max_user:
            max_user = user
            max_value = value
        elif user == max_user and value > max_value:
            max_value = value
            
    return [max_user, max_value]