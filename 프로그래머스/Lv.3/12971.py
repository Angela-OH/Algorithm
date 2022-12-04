def solution(sticker):
    answer = 0
    dp = [0 for _ in range(len(sticker))]
    
    if len(sticker) == 1:
        return sticker[0]
    
    # 1번 스티커를 떼는 경우 (마지막 스티커 뗄 수 x)
    dp[1] = sticker[0]
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i - 1])
    case1 = dp[-1]
    
    # 1번 스티커를 떼지 않는 경우 (마지막 스티커 뗄 수 o)
    dp[1] = sticker[1]
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    case2 = dp[-1]
    
    answer = case1 if case1 >= case2 else case2
    return answer