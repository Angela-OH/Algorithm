def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            b_number = bin(number)
            for i in range(len(b_number) - 1, 0, -1):
                if b_number[i] in ['0', 'b']:
                    answer.append(number + pow(2, len(b_number) - i - 2))
                    break
                
    return answer