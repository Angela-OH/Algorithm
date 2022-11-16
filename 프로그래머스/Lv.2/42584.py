def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            index = stack.pop()
            answer[index] = i - index 
        stack.append(i)
        
    while stack:
        index = stack.pop()
        answer[index] = len(prices) - index - 1
        
    return answer