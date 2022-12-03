def solution(gems):
    start, end = 0, 0
    min, answer = 100000, []
    gem_count = 0
    gem_type = {g:[] for g in list(set(gems))}
    
    while end <= len(gems):
        if gem_count == len(gem_type):
            gem_type[gems[start]].remove(start)
            if not gem_type[gems[start]]:
                gem_count -= 1
                if end - start < min:
                    min = end - start
                    answer = [start + 1, end]
            start += 1
        else:
            if end < len(gems):
                if not gem_type[gems[end]]:
                    gem_count += 1
                gem_type[gems[end]].append(end)
            end += 1
    return answer