t = int(input())
for i in range(t):
    w = input().strip()
    k = int(input())
    dict = {}
    answer1, answer2 = 10**4, 0

    for i in range(len(w)):
        if w[i] in dict:
            dict[w[i]].append(i)
        else:
            dict[w[i]] = [i]
    
    for d in dict:
        if len(dict[d]) < k:
            continue
        
        for i in range(len(dict[d]) - k + 1):
            count = dict[d][i + k - 1] - dict[d][i] + 1
            if count < answer1:
                answer1 = count
            if count > answer2:
                answer2 = count
        
    if answer1 == 10**4 and answer2 == 0:
        print(-1)
    else:
        print("{} {}".format(answer1, answer2))
    
        

