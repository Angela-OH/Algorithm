def produce(x_val, y_val):
    answer = ''
    if x_val > 0: # 아래
        answer += ('d' * x_val)
    if y_val < 0: # 왼
        answer += ('l' * -y_val)
    if y_val > 0: # 오
        answer += ('r' * y_val)
    if x_val < 0: # 위
        answer += ('u' * -x_val)
        
    return answer

def solution(n, m, x, y, r, c, k):
    answer = ''
    x_val, y_val = r - x, c - y
    dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
    alpha = ['d', 'l', 'r', 'u']
    op = {'d': 'u', 'u': 'd', 'r': 'l', 'l': 'r'}
    val = k - (abs(x_val) + abs(y_val))
    
    if val < 0 or val % 2 != 0: # k보다 이동해야 할 거리가 더 큼 or 왔다갔다 불가
        answer = "impossible"
    elif val == 0:
        answer = produce(x_val, y_val)
    else:
        str = produce(x_val, y_val) 
        left = {'d': 0, 'l': 0, 'r': 0, 'u': 0} # 필수로 들어가야 할 요소
        left_cnt = len(str) # 사용해야 할 문자 숫자
        for s in str:
            left[s] += 1
    
        while k - len(answer) != left_cnt:
            for i in range(4):
                if 1 <= x + dx[i] <= n and 1 <= y + dy[i] <= m:
                    if left[alpha[i]] > 0:
                        left[alpha[i]] -= 1
                        left_cnt -= 1
                    else:
                        left[op[alpha[i]]] += 1
                        left_cnt += 1
                    answer += alpha[i]
                    x += dx[i]
                    y += dy[i]
                    break
        
        for l in left:
            if left[l] > 0:
                answer += (l * left[l])
        
    return answer