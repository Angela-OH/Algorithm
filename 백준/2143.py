import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
sum_a = []

for i in range(n):
    sum = a[i]
    sum_a.append(sum)
    for j in range(i + 1, n):
        sum += a[j]
        sum_a.append(sum)
        
sum_a.sort()

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
sum_b = []

for i in range(m):
    sum = b[i]
    sum_b.append(sum)
    for j in range(i + 1, m):
        sum += b[j]
        sum_b.append(sum)
        
sum_b.sort()

count = 0
sum = 0
top, bottom = 0, len(sum_b) - 1

while top < len(sum_a) and bottom >= 0:
    val_a, val_b = sum_a[top], sum_b[bottom]
    sum = val_a + val_b
    if sum == t:
        a_count, b_count = 0, 0
        while top < len(sum_a) and sum_a[top] == val_a:
            top += 1
            a_count += 1
        while bottom >= 0 and sum_b[bottom] == val_b:
            bottom -= 1
            b_count += 1
        count += a_count * b_count
    elif sum < t:
        top += 1
    else:
        bottom -= 1

print(count)


