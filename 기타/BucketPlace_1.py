def solution(nums):
    left = [False for _ in range(len(nums))]
    right = [False for _ in range(len(nums))]

    min_v = nums[0]
    for i in range(1, len(nums)):
        min_v = min(min_v, nums[i])
        if nums[i] > min_v:
            left[i] = True

    max_v = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        max_v = max(max_v, nums[i])
        if nums[i] < max_v:
            right[i] = True
    
    for i in range(len(nums)):
        if left[i] and right[i]:
            return True

    return False

nums1 = [1, 3, 5, 7, 9]
nums2 = [5, 4, 3, 2, 1]

print(solution(nums1))
print(solution(nums2))