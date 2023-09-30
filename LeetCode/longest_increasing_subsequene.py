def BinarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
            left = mid + 1

        elif target < nums[mid]:
            right = mid - 1

    
    return left

if __name__ == '__main__':
    nums = [2, 5, 6, 8, 9, 10, 13, 16, 18]
    target = 14
    index = BinarySearch(nums, target)
    print(index)