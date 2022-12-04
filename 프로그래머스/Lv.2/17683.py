import re

def solution(m, musicinfos):
    answer = '(None)'
    max = 0
    p = re.compile('[A-Z]?[#]?')
    m = p.findall(m)
    m = ' '.join(m)

    for i, info in enumerate(musicinfos):
        infos = musicinfos[i].split(',')
        start, end = infos[0], infos[1]
        hour = int(end[:2]) - int(start[:2])
        if end[3:] >= start[3:]:
            min = int(end[3:]) - int(start[3:])
            min += hour * 60
        else:
            min = 60 - int(start[3:]) + int(end[3:])
            min += (hour - 1) * 60
        title = infos[2]
        melody = p.findall(infos[3])[:-1]
        melody = melody * (min // len(melody)) + melody[:min % len(melody)] + [' ']
        melody = ' '.join(melody)

        if m in melody:
            if min > max:
                max = min
                answer = title
                
    return answer