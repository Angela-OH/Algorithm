def main():
    sentence = input()
    b = []
    min = 1000 

    for i, s in enumerate(sentence):
        if s == 'b':
            b.append(i)

    b_cnt = len(b)
    total_cnt = len(sentence)
    if b_cnt == total_cnt:
        return 0
    if not b:
        return 0

    for i in range(b[0], b[-1] + 1):
        left, right = i, (i + b_cnt - 1) % total_cnt
        cnt = 0
        if left < right:
            for b_index in b:
                if not (left <= b_index <= right):
                    cnt += 1
        else:
            for b_index in b:
                if right < b_index < left:
                    cnt += 1
        if cnt < min:
            min = cnt

    return min

print(main())