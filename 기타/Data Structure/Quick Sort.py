import sys
sys.setrecursionlimit(10 ** 6)

def quick_sort(arr, start, end): # O(n * logn), 만약 편향된 정렬 -> O(n ** 2) => pivot의 선정이 중요함
    if start >= end:
        return

    pivot = start
    left, right = start + 1, end
    
    while left <= right:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[right], arr[pivot] = arr[pivot], arr[right]
    
    # right만 현재 정렬이 되었음
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

arr = [5, 1, 45, 2, -3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)