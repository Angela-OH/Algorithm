import math

def solution(fees, records):
    answer = []
    park = {}
    for record in records:
        record = record.split(" ")
        time, num = record[0], record[1]
        if num in park:
            park[num].append(time)
        else:
            park[num] = [time]
    for p in park:
        if len(park[p]) % 2 != 0:
            park[p].append('23:59')
    park = sorted(park.items())
    
    for p, time in park:
        time_sum, fare_sum = 0, 0
        
        for i in range(1, len(time), 2):
            hr = int(time[i][:2]) - int(time[i - 1][:2])
            m = int(time[i][3:]) - int(time[i - 1][3:])
            time_sum += hr * 60 + m
            
        if time_sum > fees[0]:
            fare_sum = fees[1] + math.ceil((time_sum - fees[0]) / fees[2]) * fees[3]
        else:
            fare_sum = fees[1]
            
        answer.append(fare_sum)
        
    return answer