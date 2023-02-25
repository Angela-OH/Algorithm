import math

def calculate_minute(start, end):
    return 60 * (int(end[:2]) - int(start[:2])) + int(end[3:]) - int(start[3:])

def solution(fees, records):
    detail = {}
    answer = []
    
    for record in records:
        r = record.split()
        if r[1] not in detail:
            detail[r[1]] = [r[0]]
        else:
            detail[r[1]].append(r[0])

    for d in sorted(detail.keys()):
        if len(detail[d]) % 2 != 0:
            detail[d].append("23:59")
            
        sum = 0
        for i in range(0, len(detail[d]), 2):
            sum += calculate_minute(detail[d][i], detail[d][i + 1])
        
        if sum <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((sum - fees[0]) / fees[2]) * fees[3])
            
    return answer