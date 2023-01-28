def load(cap, arr, idx):
    cnt = 0
    while idx >= 0 and cnt < cap:
        if arr[idx] == 0:
            idx -= 1
            continue
        if cnt + arr[idx] <= cap:
            cnt += arr[idx]
            arr[idx] = 0
            idx -= 1
        else:
            arr[idx] -= (cap - cnt)
            cnt = cap
    return idx

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx, p_idx = n - 1, n - 1
            
    while (d_idx != -1 or p_idx != -1):
        while (d_idx >= 0 and deliveries[d_idx] == 0): d_idx -=1
        while (p_idx >= 0 and pickups[p_idx] == 0): p_idx -=1
        answer += (max(d_idx, p_idx) + 1) * 2 # 왕복
        d_idx = load(cap, deliveries, d_idx)
        p_idx = load(cap, pickups, p_idx)
 
    return answer