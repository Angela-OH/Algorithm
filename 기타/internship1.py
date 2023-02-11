def solution(logs):
    logs = logs.split("\n")
    answer = [0 for _ in range(24)]
    for log in logs:
        hour = int(log[11:13]) # UTC
        k_hour = (hour + 9) % 24 # UTC + 9:00
        answer[k_hour] += 1
    return answer