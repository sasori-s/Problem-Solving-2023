def findMajorityElement(nums):
    m = -1
    i = 0

    for j in range(len(nums)):
        if i == 0:
            m = nums[j]
            i = 1

        elif m == nums[j]:
            i += 1

        else:
            i -= 1
        
    return m


if __name__ == "__main__":
    nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
    print("The majority element is", findMajorityElement(nums))