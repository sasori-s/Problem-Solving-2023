def findDuplicate(nums):
    duplicate = -1

    for i in range(len(nums)):
        k = -nums[i] if nums[i] < 0 else nums[i]

        if nums[k] >= 0:
            nums[k] = -nums[k]

        else:
            duplicate = k
            break

    for i in range(len(nums)):
        nums[i] = -nums[i]

    return duplicate

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 2]

    print(f"The duplicate element is {findDuplicate(nums)}")