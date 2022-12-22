import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    inputs = []
    max = 0
    for i in range(t):
        n = int(input())
        if n > max:
            max = n
        inputs.append(n)

    dp = [0 for _ in range(max + 1)]
    dp[0] = 1
    money = [1, 2, 3]
    for m in money:
        for d in range(m, n + 1):
            dp[d] += dp[d - m]
    
    for i in inputs:
        print(dp[i])