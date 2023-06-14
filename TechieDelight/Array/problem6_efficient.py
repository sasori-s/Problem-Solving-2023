def findMaxLenSublist(nums, S):
    length = 0
    ending_index = -1
    d = {}
    d[0] = -1
    target = 0

    for i in range(len(nums)):
        target += nums[i]

        if target not in d:
            d[target] = i

        if target - S in d and length < i -  d[target - S] :
            length = i - d[target - S]
            ending_index = i

    print((ending_index - length + 1, ending_index))


if __name__ == '__main__':
 
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8
 
    findMaxLenSublist(nums, target)