def cache_hit(stack, city):
    del stack[stack.index(city)]
    stack.append(city)
    return stack

def cache_miss(stack, city, cacheSize):
    if cacheSize == 0:
        return stack
    if len(stack) == cacheSize:
        stack.pop(0)
    stack.append(city)
    return stack

def solution(cacheSize, cities):
    answer = 0
    stack = []
    for city in cities:
        city = city.lower()
        if city in stack:
            stack = cache_hit(stack, city)
            answer += 1
        else:
            stack = cache_miss(stack, city, cacheSize)
            answer += 5
    return answer