def gap(a, b): # b가 a보다 무조건 뒤 날짜임 (ex. 20220502, 20220504)
    a_year, a_month, a_day = int(a[:4]), int(a[4:6]), int(a[:8])
    b_year, b_month, b_day = int(b[:4]), int(b[4:6]), int(b[:8])
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if a_year < b_year:
        sum = 365 * (b_year - a_year - 1)
        sum += (day[a_month - 1] - a_day + 1 + b_day)
        for i in range(a_month + 1, 13):
            sum += day[i - 1]
        for i in range(b_month - 1):
            sum += day[i - 1]
        return sum

    elif a_month < b_month:
        sum = a_day + b_day
        for i in range(a_month + 1, b_month):
            sum += day[i - 1]
        return sum
    else:
        return b_day - a_day

def solution(mask, dates):
    date_num = []
    for date in dates:
        date = date.replace("/", "")
        if "~" in date:
            date = date.split("~")
            for i in range(int(date[0]), int(date[1]) + 1):
                if str(i) not in date_num:
                    date_num.append(str(i))
        else:
            if date not in date_num:
                date_num.append(date)
    date_num.sort()
    print(date_num)
    date_ox = []
    for i in range(len(date_num)):
        date_ox.append(gap(date_num[0], date_num[i]))

    return date_ox

m1 = [[3200, 4], [2300, 2], [1100, 1], [4200, 6]]
d1 = ["2022/05/02", "2022/05/01", "2022/05/07", "2022/05/05", "2022/05/08", "2022/05/13~2022/05/15", "2022/05/14~2022/05/17", "2022/05/01~2022/05/02", "2022/05/16"]
m2 = [[600, 2], [500, 1], [1015, 400]]
d2 = ["2023/01/01~2023/01/02", "2021/12/31"]
m3 = [[3651, 365], [10, 1]]
d3 = ["2025/01/01~2025/12/31"]
print(solution(m1, d1))
print(solution(m2, d2))