import string

def calculate(a, b):
    alpha = {ascii: i for i, ascii in enumerate(list(string.ascii_uppercase))}
    x1, y1 = alpha[a] // 6, alpha[a] % 6
    x2, y2 = alpha[b] // 6, alpha[b] % 6
    return abs(x1 - x2) + abs(y1 - y2)

def solution(sentence):
    answer = 10 ** 6                                                                  
    # 첫글자는 무조건 왼손 할당
    # 오른손 할당을 시작할 문자를 1개 더 정해야함
    for i in range(1, len(sentence)):
        leftWord = sentence[0]
        cnt = 0
        for j in range(1, len(sentence)):
            if j < i:
                cnt += calculate(leftWord, sentence[j])
                leftWord = sentence[j]
            elif i == j:
                rightWord = sentence[i]
            else:
                left = calculate(leftWord, sentence[j])
                right = calculate(rightWord, sentence[j])
                if left <= right:
                    leftWord = sentence[j]
                    cnt += left
                else:
                    rightWord = sentence[j]
                    cnt += right

        answer = min(answer, cnt)

    return answer

print(solution("HAPPY"))
print(solution("HACN"))
print(solution("CAKE"))
print(solution("HABCDP"))