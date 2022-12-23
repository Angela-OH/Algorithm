if __name__ == "__main__":
    n, d = map(int, input().split())
    dp = [i for i in range(d + 1)]
    op = []
    for i in range(n):
        start, end, dis = map(int, input().split())
        op.append((start, end, dis))
    op.sort()
    for start, end, dis in op:
        if end <= d:
            dp[end] = min(dp[end], dp[start] + dis)
            for j in range(end + 1, d + 1):
                dp[j] = min(dp[j], dp[end] + (j - end))
    
    print(dp[d])
