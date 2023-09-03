def findMaxLengthSublists(nums, S):
    lenght = 0
    ending_index = -1

    target = 0

    d = {}
    d[0] = -1

    for i in range(len(nums)):
        target += nums[i]

        if target not in d:
            d[target] = i

        if target - S in d and lenght < i - d[target - S] :
            lenght = i - d[target - S]
            ending_index = i

    print((ending_index - lenght + 1, ending_index))


if __name__ == '__main__':
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8

    findMaxLengthSublists(nums, target)