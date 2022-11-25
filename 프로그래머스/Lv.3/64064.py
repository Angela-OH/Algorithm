def solution(user_id, banned_id):
    answer = 0
    dic = {b: [] for b in banned_id}
    for index, user in enumerate(user_id):
        for banned in banned_id:
            cnt = 0
            if len(user) != len(banned):
                continue
            for i in range(len(user)):
                if banned[i] == '*':
                    continue
                if banned[i] != user[i]:
                    cnt = 1
                    break
            if cnt == 0:
                if index not in dic[banned]:
                    dic[banned].append(index)
    ans_list = []
    stack = []
    for i, v in enumerate(dic[banned_id[0]]):
        stack.append((v, 0))
        
    ans = [-1 for _ in range(len(banned_id))]
    while stack:
        result, index = stack.pop()
        if result in ans[:index]:
            continue
        ans[index] = result
        if index == len(banned_id) - 1:
            ans_list.append(ans[:])
            continue
        for d in dic[banned_id[index + 1]]:
            if result == d and d in ans:
                continue
                
            stack.append((d, index + 1))

    for l in list(set([tuple(set(ans)) for ans in ans_list])):
        if len(l) < len(banned_id):
            continue
        answer += 1 
        
    return answer