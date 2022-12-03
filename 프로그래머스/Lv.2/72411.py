import itertools
from collections import Counter

def compare(a, b):
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    menu = ''
    menu_list = []
    index_a, index_b = 0, 0
    
    while index_a < len(a) and index_b < len(b):
        if a[index_a] == b[index_b]:
            menu += a[index_a]
            index_a += 1 
            index_b += 1
        elif a[index_a] < b[index_b]:
            index_a += 1
        else:
            index_b += 1
            
    for i in range(2, len(menu) + 1):
        for j in list(itertools.combinations(menu, i)):
            s = ''
            for k in j:
                s += k
            menu_list.append(s)
            
    return menu_list

def solution(orders, course):
    answer = []
    course_list = []
    for a, b in list(itertools.combinations(orders, 2)):
        menu_list = compare(a, b)
        for menu in menu_list:
            if len(menu) in course:
                course_list.append(menu)
    
    counter = Counter(course_list)
    counter = counter.most_common()
    for c in course:
        max = 0
        for count in counter:
            if len(count[0]) != c:
                continue
            if count[1] >= max:
                max = count[1]
                if count[0] not in answer:
                    answer.append(count[0])
    answer.sort()
    return answer