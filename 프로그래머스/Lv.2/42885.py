def solution(people, limit):
    people.sort()
    start, end = 0, len(people) - 1
    sum = people[end]
    answer = 0
    while start <= end:
        if start == end:
            answer += 1
            break
        if limit == sum + people[start]:
            answer += 1
            end -= 1
            start += 1
            sum = people[end]
        elif limit < sum + people[start]:
            answer += 1
            end -= 1
            sum = people[end]
        else:
            sum += people[start]
            start += 1
    return answer