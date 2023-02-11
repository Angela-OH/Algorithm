def solution(lotteries):
    answer = 0
    max_possibility = 0
    max_price = 0
    possibility = []

    for lottery in lotteries:
        if (lottery[1] + 1) <= lottery[0]:
            possibility.append(1)
        else:
            possibility.append(lottery[0]/(lottery[1] + 1))

    for i, p in enumerate(possibility):
        if p > max_possibility:
            max_possibility = p
            max_price = lotteries[i][2]
            answer = i + 1
        elif p == max_possibility:
            if lotteries[i][2] > max_price:
                max_price = lotteries[i][2]
                answer = i + 1
    return answer