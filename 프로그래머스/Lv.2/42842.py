def solution(brown, yellow):
    x = 3
    while True:
        y = (brown + 4) / 2 - x
        if x * y == brown + yellow:
            break
        x += 1
    if x > y:
        answer = [x, y]
    else:
        answer = [y, x]
    return answer