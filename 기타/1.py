def isQR(img, height, width, n, low, high):
    black = 0
    
    for i in range(height, height + n):
        for j in range(width, width + n):
            if i == height or j == width or i == (height + n - 1) or j == (width + n - 1):
                if img[i][j] != '#':
                    return False
            elif img[i][j] == '#':
                black += 1

    if low * pow((n - 2), 2) / 100 <= black < high * pow((n - 2), 2) / 100:
        return True
    else:
        return False


def solution(low, high, img):
    answer = 0
    width, height = len(img[0]), len(img)
    max_n = min([width, height])

    for i in range(height):
        for j in range(width):
            for k in range(3, max_n + 1):
                if i + k > height or j + k > width:
                    break
                if isQR(img, i, j, k, low, high):
                    answer += 1
                
    return answer

print(solution(25, 51, [".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]))