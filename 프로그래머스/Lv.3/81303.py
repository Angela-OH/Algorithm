def solution(n, k, cmd):
    visited = ['O' for _ in range(n)]
    linked = [[i - 1, i + 1] for i in range(n)]
    stack = []
    for cmd_input in cmd:
        c = cmd_input.split(" ")
        if c[0] == 'U' or c[0] == 'D':
            for i in range(int(c[1])):
                if c[0] == 'U':
                    k = linked[k][0]
                else:
                    k = linked[k][1]
        elif c[0] == 'C':
            stack.append(k)
            visited[k] = 'X'
            if linked[k][0] != -1:
                linked[linked[k][0]][1] = linked[k][1]
            if linked[k][1] != n:
                linked[linked[k][1]][0] = linked[k][0]
            
            if linked[k][1]  == n:
                k = linked[k][0]
            else:
                k = linked[k][1]
        elif c[0] == 'Z':
            latest_delete = stack.pop()
            visited[latest_delete] = 'O'
            if linked[latest_delete][0] != -1:
                linked[linked[latest_delete][0]][1] = latest_delete
            if linked[latest_delete][1] != n:
                linked[linked[latest_delete][1]][0] = latest_delete
    return ''.join(visited)