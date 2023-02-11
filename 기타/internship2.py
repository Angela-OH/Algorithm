def search(boundary, target):
    start, end = 0, len(boundary) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == boundary[mid][0]:
            return mid
        elif target > boundary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1
    return end

def solution(money, minratio, maxratio, ranksize, threshold, months):
    boundary = []

    if threshold > 0: # threshold가 0이 아닌 경우라면 threshold 미만 금액대 필요
        boundary.append((0, 0))
    for i in range(maxratio-minratio + 1):
        boundary.append((threshold + ranksize * i, minratio + i))
    #print(boundary)

    for i in range(months):
        abstract_money = (money - money % 100) # 소유 가정 금액
        index = search(boundary, abstract_money)
        rate = boundary[index][1]
        money = int(money - abstract_money * (rate / 100))
    
    return money