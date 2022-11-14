def solution(priorities, location):
    index, cnt = 0, 0
    while True:
        if priorities[index] != max(priorities):
            index = (index + 1) % len(priorities)
        else:
            cnt += 1
            del priorities[index]
            if location == index:
                break
            elif location > index:
                location -= 1
            if index == len(priorities):
                index = 0
    return cnt