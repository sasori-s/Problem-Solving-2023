def findPair(nums, target):
    d = {}

    for i, e in enumerate(nums):
        if target - e in d:
            print("Pair found at", (nums[d.get(target - e)]), nums[i])
            return 

        d[e] = i

    print("Pair not found")


if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)