import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
word = []
extra = []
answer = 0

# 초기값
basic = 0
basic |= (1 << (ord('a') - ord('a')))
basic |= (1 << (ord('c') - ord('a')))
basic |= (1 << (ord('i') - ord('a')))
basic |= (1 << (ord('n') - ord('a')))
basic |= (1 << (ord('t') - ord('a')))
cnt = 5

total_basic = basic
for i in range(n):
    str = input()
    new_basic = basic
    for i in range(4, len(str) - 4):
        new_basic |= (1 << (ord(str[i]) - ord('a')))
        if (total_basic & (1 << (ord(str[i]) - ord('a')))) == 0:
            cnt += 1
            total_basic |= (1 << (ord(str[i]) - ord('a')))
            extra.append(str[i])
    word.append(new_basic)

if k < 5: # 한 단어도 읽을 수가 없음
    print(0)
    exit()

if cnt <= k: # 모든 단어를 읽을 수 있음
    print(n)
    exit()

for comb in list(combinations(extra, k - 5)):
    new_basic = basic
    sum = 0
    for c in comb:
        new_basic |= (1 << (ord(c) - ord('a')))
    for w in word:
        if (new_basic | w) == new_basic:
            sum += 1
    answer = max(answer, sum)

print(answer)
    