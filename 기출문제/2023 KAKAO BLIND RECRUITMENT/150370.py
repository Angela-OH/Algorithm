def calculate(now, add_month):
    year, month, day = int(now[:4]), int(now[5:7]), int(now[8:])
    # 약관 더해주기
    if month + add_month <= 12:
        month += add_month
    else:
        year += (month + add_month) // 12
        month = (month + add_month) % 12
        if month == 0: 
            month = 12
            year -= 1
    
    # 하루 빼기
    if day == 1: # 1일인 경우
        if month == 1: # 1월인 경우
            year -= 1
            month = 12 # 전년도 12월로
        else: # 아닌 경우
            month -= 1 # 지난 달로
        day = 28 # 마지막 일
    else:
        day -= 1
    
    return "{0:04d}.{1:02d}.{2:02d}".format(year, month, day)

def solution(today, terms, privacies):
    answer = []
    terms = {term.split()[0]: int(term.split()[1]) for term in terms}
    for i, privacy in enumerate(privacies):
        date = privacy.split()[0]
        term = privacy.split()[1]
        if today > calculate(date, terms[term]):
            answer.append(i + 1)
    return answer