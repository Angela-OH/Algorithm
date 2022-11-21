def dfs(n, words):
    word = [0 for _ in range(n + 1)]
    cnt = 0
    
    for t in range(1, 6):
        stack = []
        stack.append((t, 0))
    
        while stack:
            w, i = stack.pop()
            word[i] = w
            cnt += 1
            if word[:i + 1] == words:
                return cnt
            if i == n - 1:
                continue
            for j in range(n, 0, -1):
                stack.append((j, i + 1))

def solution(word):
    length = len(word)
    dic = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    words = []
    for w in word:
        words.append(dic[w])
    
    return dfs(5, words)