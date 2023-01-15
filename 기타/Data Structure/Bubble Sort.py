def bubble_sort(arr): # O(n**2)
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    
    return arr

arr = [5, 4, 2, 7, 5, -1]
print(bubble_sort(arr))
