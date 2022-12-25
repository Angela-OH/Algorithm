import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    #num.sort(key = lambda x: abs(x))
    min_v = sys.maxsize
    idx = (0, 0)

    ''' 방법 1
    for i in range(1, len(num)):
        sum = abs(num[i - 1] + num[i])
        if sum < min_v:
            min_v = sum
            idx = (num[i - 1], num[i])
    
    first = min(idx)
    second = max(idx)
    '''

    # 방법 2
    start, end = 0, n - 1
    while start < end:
        sum = num[end] + num[start]
        if sum == 0:
            idx = (start, end)
            break
        if abs(sum) < min_v:
            min_v = abs(sum)
            idx = (start, end)
        if sum > 0:
            end -= 1
        else:
            start += 1
        
    first, second = num[idx[0]], num[idx[1]]

    print("{} {}".format(first, second))