import math

min, max = map(int, input().split())
isPrime = [True for _ in range(max - min + 1)]
answer = max - min + 1

for i in range(2, int(math.sqrt(max)) + 1):
    index = i ** 2
    val = math.ceil(min/index) # isPrime의 시작 index는 min -> 체크할 수 있는 범위 수정 필요
    for j in range(val * index, max + 1, index):
        if not isPrime[j - min]:
            continue
        isPrime[j - min] = False
        answer -= 1

print(answer)





