import math

def solution(enroll, referral, seller, amount):
    answer = []
    index = {e: i for i, e in enumerate(enroll)}
    income = [0 for _ in range(len(enroll))]
    amount = [a * 100 for a in amount]
    for i in range(len(seller)):
        name = seller[i]
        price = amount[i]
        while True:
            ref_name = referral[index[name]]
            ref = math.floor(price * 0.1)
            income[index[name]] += (price - ref)
            if ref_name == "-" or ref == 0:
                break
            name = ref_name
            price = ref
    return income