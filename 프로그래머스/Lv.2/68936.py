def solution(a):
    answer = [0, 0]

    def compact(arr):
        n = len(arr)
        if n == 1:
            answer[arr[0][0]] += 1
            return

        cnt = 0
        num = arr[0][0]
        for i in range(n):
            for j in range(n):
                if arr[i][j] != num:
                    cnt += 1
        if cnt == 0:
            answer[num] += 1
        else:
            m = n // 2
            compact([arr[:m][i][:m] for i in range(m)]) # 위쪽 왼
            compact([arr[m:][i][:m] for i in range(m)]) # 아래쪽 왼
            compact([arr[:m][i][m:] for i in range(m)]) # 위쪽 오른
            compact([arr[m:][i][m:] for i in range(m)]) # 아래쪽 오른
   
    compact(a)
    
    return answer