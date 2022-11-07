def solution(buildings):
    answer = []
    visited = {'n': 0, 'a': 0, 'k': 0}

    for building in buildings:
        count = 0
        for b in building:
            if b in visited:
                visited[b] = 1
                if b == 'k':
                    if list(visited.values()) == [1, 1, 1]:
                        count += 1
                        for v in visited:
                            visited[v] = 0
        if count == 2:
            answer.append("O")
        else:
            answer.append("X")

    return answer

'''
ex1 = ["sungsoo_naknak", "sungsoo_naknaknak", "sungsoo_nak"]
ex2 = ["i_am_not_a_kim_and_not_awk", "nananananakkkk"]
ex3 = ["nnnnnnnaaknak"]
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
'''
