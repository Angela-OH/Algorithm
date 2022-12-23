import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, s = map(int, input().split())
    num = list(map(int, input().split()))


    start, end = 0, 0
    sum = num[end]
    min = n + 1
    while end < n:
        if sum < s:
            end += 1
            if end < n:
                sum += num[end]
        else:
            if end - start + 1 < min:
                min = end - start + 1
            sum -= num[start]
            start += 1
    if min == n + 1:
        print(0)
    else:
        print(min)