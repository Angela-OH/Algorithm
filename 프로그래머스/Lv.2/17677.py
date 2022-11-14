def make_combination(sentence):
    dict = {}
    for i in range(len(sentence) - 1):
        block = sentence[i : i + 2].lower()
        if not block.isalpha():
            continue
        if block in dict:
            dict[block] += 1
        else:
            dict[block] = 1

    return dict

def solution(str1, str2):
    dict1, dict2 = make_combination(str1), make_combination(str2)
    i, u = 0, 0
    i_key = set(dict1.keys()).intersection(set(dict2.keys()))
    u_key = set(dict1.keys()).union(set(dict2.keys()))

    if not i_key and not u_key: # 공집합인 경우
        return 65536
    
    for key in i_key:
        i += min(dict1[key], dict2[key])
    
    for key in u_key:
        if key in dict1 and key in dict2:
            u += max(dict1[key], dict2[key])
        elif key in dict1:
            u += dict1[key]
        else:
            u += dict2[key]

    return int(65536 * (i / u))