def gcd(a, b):
    if b > a:
        tmp = b
        b = a 
        a = tmp
    while b > 0:
        a, b = b, a % b
    return a

def solution(w,h):
    return w * h - (w + h - gcd(w, h))