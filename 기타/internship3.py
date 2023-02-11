def open_room(rooms, visited, index):
    cnt, open_index = 0, index
    while True:
        if open_index == index and cnt != 0:
            break
        open_index = rooms[open_index] 
        visited[open_index] = 1
        cnt += 1
    return visited

def master_key(rooms, visited):
    count = 0
    for i in range(len(rooms)):
        if visited[i] == 0:
            visited = open_room(rooms, visited, i)
            count += 1
    return count

def solution(rooms):
    answer = 200001
    visited = [0 for _ in range(len(rooms))]
    rooms = [(room - 1) for room in rooms]
    
    # 열쇠 교체 x
    result = master_key(rooms, visited)
    if result < answer:
        answer = result

    # 열쇠 교체 o
    if answer > 1:
        answer -= 1

    return answer