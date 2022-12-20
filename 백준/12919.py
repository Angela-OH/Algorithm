import sys
sys.setrecursionlimit(10 ** 6)

if __name__ == "__main__":
    s = input()
    t = input()
    answer = 0

    def change(s, t):
        global answer
        if len(s) == len(t):
            if s == t:
                answer = 1
                return 
            else:
                return
        
        if t[-1] == 'A':
            change(s, t[:-1])

        if t[0] == 'B':
            change(s, t[1:][::-1])
            
    change(s, t)
    if answer == 0:
        print(0)
    else:
        print(1)