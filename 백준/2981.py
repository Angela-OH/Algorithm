def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def div(x):
    result = [x]
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: # x = A * B
            result.append(i) # A를 구함
            if i ** 2 != x: # B를 구함 (A * A인 경우는 제외)
                result.append(x // i)
    result.sort()
    return result

n = int(input())
num = [int(input()) for _ in range(n)]
diff = []
num.sort(reverse = True)

for i in range(1, n):
    diff.append(num[i - 1] - num[i])

if len(diff) == 1:
    answer = diff[0]
elif len(diff) == 2:
    answer = gcd(diff[0], diff[1])
else:
    answer = diff[0]
    for i in range(1, len(diff)):
        answer = gcd(answer, diff[i])

for i in div(answer):
    print(i, end = ' ')


