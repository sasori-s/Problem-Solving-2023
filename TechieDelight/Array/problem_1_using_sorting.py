def find_pair(nums, target):
    nums.sort()
    low, high = (0, len(nums) - 1)

    while high > low:
        if nums[low] + nums[high] == target:
            print(f"The pain has been found of {(nums[low], nums[high])}")
        
        if nums[low] + nums[high] > target:
            high -= 1
        
        else:
            low += 1


nums = [8, 7, 2, 5, 3, 1]
target = 10

find_pair(nums, target)
    