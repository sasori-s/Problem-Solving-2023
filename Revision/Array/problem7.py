def findLargestSublists(nums):
    largest = 0
    ending_index = -1

    d = {}
    d[0] = -1

    total = 0

    for i in range(len(nums)):
        total += -1 if nums[i] == 0 else 1

        if total in d and largest < i - d.get(total):
            largest = i - d.get(total)
            ending_index = i

        else:
            d[total] = i

    if ending_index != -1:
        print(f"The largest subarray is {(ending_index - largest + 1, ending_index)}")
    else:
        print('No subarray exists')

if __name__ == '__main__':
    nums = [0, 0, 1, 0, 1, 0, 0]
    findLargestSublists(nums)