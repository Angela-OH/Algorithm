def RC_operation(type):
    global max_row, max_column

    if type == 0: # r operation
        outer, inner = max_row, max_column
        new_row, new_column = max_row, 0
    else: # c operation
        outer, inner = max_column, max_row
        new_row, new_column = 0, max_column

    for i in range(outer):
        dict = {}
        for j in range(inner):
            if type == 0:
                value = arr[i][j]
            else:
                value = arr[j][i]

            if value == 0:
                continue
            if value in dict:
                dict[value] += 1
            else:
                dict[value] = 1

        orders = sorted(dict, key = lambda x: (dict[x], x))

        new_array = []
        for order in orders:
            new_array.append(order)
            new_array.append(dict[order])
        if len(new_array) > 100:
            new_array = new_array[:100]

        if type == 0:
            for u in range(len(new_array)):
                arr[i][u] = new_array[u]
            for u in range(len(new_array), max_column):
                arr[i][u] = 0
            if len(new_array) > new_column:
                new_column = len(new_array)
        else:
            for u in range(len(new_array)):
                arr[u][i] = new_array[u]
            for u in range(len(new_array), max_row):
                arr[u][i] = 0
            if len(new_array) > new_row:
                new_row = len(new_array)
    
    max_row, max_column = new_row, new_column

def operation():
    count = 0

    while True:
        if arr[r - 1][c - 1] == k:
            return count
        if count > 100:
            return -1
        count += 1
        if max_row >= max_column:
            RC_operation(0)
        else:
            RC_operation(1)  

r, c, k = map(int, input().split())
arr = [[0 for _ in range(100)] for _ in range(100)]
max_row, max_column = 3, 3

for i in range(3):
    input_v = list(map(int, input().split()))
    for j in range(len(input_v)):
        arr[i][j] = input_v[j]

print(operation())