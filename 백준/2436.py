import math

def lcm(x, y):
    return (x * y) / gcd(x, y)

def gcd(x, y):
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x

a, b = map(int, input().split())
c = b // a
sum = 200000000
result = ()

for i in range(1, int(math.sqrt(c)) + 1):
    if c % i == 0:
        if (gcd(i, c // i)) == 1:
            if i + c // i < sum:
                sum = i + c // i
                result = (i, c // i)

print(a * result[0], a* result[1])