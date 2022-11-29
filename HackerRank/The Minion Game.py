def minion_game(string):
    # your code goes here
    score_A, score_B = 0, 0
    vowels = ['A', 'E', 'U', 'O', 'I']
    word_A, word_B = [], []
    length = len(string)
    
    for i, s in enumerate(string):
        if s in vowels:
            word_A.append(i)
        else:
            word_B.append(i)
    
    for a in word_A:
        score_A += length - a 
    for b in word_B:
        score_B += length - b 
    
    if score_A == score_B:
        print('Draw')
    elif score_A > score_B:
        print('Kevin ' + str(score_A))
    else:
        print('Stuart ' + str(score_B))
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)