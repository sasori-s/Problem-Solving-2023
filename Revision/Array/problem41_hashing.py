def isTripletExist(nums, target):
    d ={}
    
    for i, e in enumerate(nums):
        d[e] = i

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            val = target - (nums[i] + nums[j])

            if val in d:
                if d[val] != i and d[val] != j:
                    return True

    return False


if __name__ == '__main__':
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 6

    if isTripletExist(nums, target):
        print("Triplet exists")
    else:
        print("Triplet does not exist")