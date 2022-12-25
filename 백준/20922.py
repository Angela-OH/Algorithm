import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    cnt = {num[0]: 1}
    answer = 0
    start, end = 0, 0
    while True:
        if cnt[num[end]] > k:
            cnt[num[start]] -= 1
            start += 1
        else:
            if end - start + 1 > answer:
                answer = end - start + 1
            end += 1
            if end == n:
                break
            if num[end] in cnt:
                cnt[num[end]] += 1
            else:
                cnt[num[end]] = 1
    
    print(answer)