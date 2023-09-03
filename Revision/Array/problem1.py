def findPair(nums, target):
    (low, high) = (0, len(nums) -1 )

    nums.sort()

    while low < high:
        if nums[low] + nums[high] == target:
            print("Pair found at  ", (nums[low], nums[high]))
            return

        if nums[low] + nums[high] < target:
            low += 1

        else:
            high -= 1

    print("Pair not found")


if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)