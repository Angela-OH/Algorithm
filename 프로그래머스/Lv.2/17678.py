def calculate(time, t, isAdd):
    hour = int(time[:2])
    minute = int(time[3:])
    if isAdd:
        if minute + t >= 60:
            hour += (minute + t) // 60
            minute = (minute + t) % 60
        else:
            minute += t
    else: # t는 1인 경우만 존재
        if minute - t < 0:
            hour -= 1
            minute = 59
        else:
            minute -= 1
    new_time = format(hour, "02") + ":" + format(minute, "02")
    return new_time

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    time = "09:00"
    index = -1
    max_people = n * m # 최대 탈 수 있는 인원
    
    while True:
        count = 0
        n -= 1
        for i in range(index + 1, len(timetable)):
            if timetable[i] <= time:
                count += 1
                index = i
                if count >= m:
                    break
            else:
                break
        max_people -= count
        if max_people <= 0:
            next_time = calculate(time, t, True)
            conn_index = index + max_people
            if timetable[conn_index] < next_time:
                answer = calculate(timetable[conn_index], 1, False)
            else:
                answer = next_time
            break
        elif n == 0:
            answer = time
            break
        else:
            max_people -= (m - count)
            time = calculate(time, t, True)
    return answer