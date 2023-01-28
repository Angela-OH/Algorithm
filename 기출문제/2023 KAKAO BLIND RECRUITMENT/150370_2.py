def calculate(date):
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    terms = {term.split()[0]: int(term.split()[1]) for term in terms}
    today = calculate(today)
    for i, privacy in enumerate(privacies):
        date = calculate(privacy.split()[0])
        term = terms[privacy.split()[1]] * 28 - 1
        if today > date + term:
            answer.append(i + 1)
        
    return answer