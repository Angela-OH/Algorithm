# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def check(binary):
    count, max = 0, 0
    for i in range(1, len(binary)):
        if binary[i] == '1':
            if count > max:
                max = count
            count = 0
            continue
        count += 1

    return max

def solution(N):
    # write your code in Python 3.8.10
    binary = format(N, 'b')
    return check(binary)

print(solution(15))