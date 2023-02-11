def solution(n, m, q, temperatures, clothes):
    answer = q
    clothes.sort() # 구간 시작점을 기준으로 정렬

    for i in range(n - m + 1): # 슬라이딩 윈도우 (구간 크기: m)
        temp = temperatures[i : i + m]
        temp.sort() # 기온이 높은 순으로 정렬

        c_max = 0
        c_count = 0
        c_idx = -1
        for t in temp:
            if t <= c_max: # 현재 옷으로 커버할 수 있는 최대 온도로 커버 가능?
                continue # 패스
            while c_idx < q: # 커버 불가능하면 커버 가능한 옷을 찾을 때까지 반복
                c_idx += 1
                c_max = max(c_max, clothes[c_idx][1])
                if clothes[c_idx][0] <= t <= clothes[c_idx][1]:
                    break
            c_count += 1
        
        answer = min(answer, c_count)

    return answer

print(solution(4, 3, 3, [25, 30, 15, 20], [[13, 21], [18, 25], [26, 30]]))