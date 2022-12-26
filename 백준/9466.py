import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

answer = 0

def dfs(num, cycle, visited, i):
    global answer
    visited[i] = 1
    cycle.append(i)

    if visited[num[i] - 1] == 0: # 아직 방문 x
        dfs(num, cycle, visited, num[i] - 1)
    elif (num[i] - 1) in cycle: # 이미 방문 o + cycle o
        answer += (len(cycle) - cycle.index(num[i] - 1))
        return

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        answer = 0
        num = list(map(int, input().split()))
        visited = [0 for _ in range(n)]

        for i in range(n):
            cycle = []
            if visited[i] == 0:
                dfs(num, cycle, visited, i)
                 
        print(n - answer)