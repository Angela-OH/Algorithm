def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse = True, key = lambda x: x*3)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)