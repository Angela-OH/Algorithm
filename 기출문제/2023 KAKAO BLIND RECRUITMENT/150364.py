def solution(edges, target):
    node_cnt = len(edges) + 1
    leaf_cnt = 0
    edge = [[] for _ in range(node_cnt)] # 자식 노드 저장
    path = [-1 for _ in range(node_cnt)] # 다음으로 이동할 자식 노드의 순번 저장
    leaf = [0 for _ in range(node_cnt)] # 리프 노드 접근 횟수 저장
    order = [[] for _ in range(node_cnt)] # 리프 노드 접근 순서 저장
    visited = [False for _ in range(node_cnt)]
    
    for e in edges:
        edge[e[0] - 1].append(e[1] - 1)
    for i in range(node_cnt):
        if len(edge[i]) >= 1: # 자식 노드가 있음
            edge[i].sort()
            path[i] = 0 # 길 표시 (0부터 시작)
        else: # 자식 노드가 없음 => 리프 노드
            leaf_cnt += 1 # 리프 노드 개수 기억해두기

    cnt = 0
    while leaf_cnt > 0:
        cur = 0 # root에서 떨어트림
        while path[cur] != -1: # 리프 노드에 도달할 때까지
            tmp = cur
            cur = edge[cur][path[cur]] # 다음 노드 찾기
            path[tmp] = (path[tmp] + 1) % len(edge[tmp]) # 새로운 길 설정
        
        order[cur].append(cnt) # 리프 노드 방문 순서 기억해두기
        cnt += 1 # 전체 리프 노드 방문 횟수 증가
        leaf[cur] += 1 # 해당 리프 노드 방문 횟수 증가
        
        if 1 * leaf[cur] <= target[cur] <= 3 * leaf[cur]: # target 값을 만들 수 있는 경우
            if not visited[cur]: # 중복 체크 방지
                visited[cur] = True
                leaf_cnt -= 1
        elif leaf[cur] > target[cur]:
            answer = [-1]
            return answer
        
    answer = [0 for _ in range(cnt)]

    for i in range(node_cnt):
        for j in range(leaf[i]):
            for k in range(1, 4, 1):
                a = target[i] - k
                b = leaf[i] - 1
                if b == 0:
                    answer[order[i][j]] = target[i]
                    break
                elif b <= a <= 3 * b:
                    target[i] -= k
                    leaf[i] -= 1
                    answer[order[i][j]] = k
                    break
            
    return answer

print(solution([[2, 4], [1, 2], [6, 11], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9], [5, 8]], [0, 0, 0, 3, 0, 0, 1, 2, 2, 2, 3]))
print(solution([[1, 2]], [0, 7]))
print(solution([[8, 11], [1, 2], [2, 3], [2, 4], [3, 6], [3, 5], [4, 7], [4, 8], [5, 9], [5, 10]], [0, 0, 0, 0, 0, 3, 4, 0, 5, 3, 5]))