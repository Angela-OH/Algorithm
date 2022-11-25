def solution(n):
    answer = []
    m = n
    triangle = [[0 for _ in range(i)] for i in range(1, n + 1)]
    index, indey = 0, 0
    count = 1
    
    while n > 0:
        if n == 1:
            triangle[index][indey] = count
        for i in range(n - 1):
            triangle[index + i][indey] = count + i 
            triangle[index + n - 1][indey + i] = count + n - 1 + i
            triangle[index + n - 1 - i][indey + n - 1 - i] = count + 2 * n - 2 + i
        count += (n * 3 - 3)
        index += 2
        indey += 1
        n -= 3
        
    for i in range(m):
        for j in range(i + 1):
            answer.append(triangle[i][j])
    return answer