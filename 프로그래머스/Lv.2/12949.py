def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    cnt = len(arr1[0])
    for x1 in range(len(arr1)):
        for y2 in range(len(arr2[0])):
            sum = 0
            for i in range(cnt):
                sum += arr1[x1][i] * arr2[i][y2]
            answer[x1][y2] = sum  
            
    return answer