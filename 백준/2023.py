def checkPrime(num):
    if num < 2:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def peculiar(p, level):
    if level == n:
        print(p)
        return

    for i in range(1, 10, 2):
        if not checkPrime(p * 10 + i):
            continue
        peculiar(p * 10 + i, level + 1)

n = int(input())
min = pow(10, n - 1)
max = pow(10, n)

for i in [2, 3, 5, 7]:
    peculiar(i, 1)