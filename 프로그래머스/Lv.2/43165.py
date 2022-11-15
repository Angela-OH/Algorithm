cnt = 0
def counting(numbers, index, isAdd, sum, target):
    global cnt
    if index == len(numbers) - 1:
        if sum == target:
            cnt += 1
        return
    counting(numbers, index + 1, 0, sum - numbers[index], target)
    counting(numbers, index + 1, 1, sum + numbers[index], target)
    
def solution(numbers, target):
    counting(numbers, -1, 0, 0, target)
    return cnt