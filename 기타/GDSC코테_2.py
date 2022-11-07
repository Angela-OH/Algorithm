def fight(a, b):
    a_potential = a[1] + b[1] * a[2]
    b_potential = b[1] + a[1] * b[2]
    
    if a_potential == b_potential:
        return -1
    elif a_potential > b_potential:
        return a[0]
    else:
        return b[0]

def solution(specs):
    result = {name: 0 for name, p, s in specs}

    for i in range(len(specs)):
        for j in range(i + 1, len(specs)):
            winner = fight(specs[i], specs[j])
            if winner != -1:
                result[winner] += 1
    answer = [i for i, value in sorted(result.items(), key = lambda x: (x[1], x[0]), reverse = True)]
    return answer

'''
ex1 = [["A", 10, 3], ["B", 20, 4], ["C", 15, 5]]
ex2 = [["GDSC", 100, 17], ["ELICE", 20, 20]]
ex3 = [["B", 10, 3], ["A", 10, 3], ["BB", 10, 3], ["AA", 10, 3]]
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
'''