def solution(queries):
    answer = []
    for query in queries:
        l = len(query)

        if l == 2:
            val = (query[1] - query[0])
        elif l == 3:
            val = (query[2] - query[0] + query[1])
        elif l == 4:
            val = (query[3] - query[0] + query[2] - query[1])
        else:
            val = (query[4] - query[0] + query[3] - query[1] + query[2])

        if val % 2 == 1:
            answer.append(1)
        else:
            answer.append(0)

    return answer