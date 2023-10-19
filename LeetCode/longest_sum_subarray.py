def subArray(nums, k):
    freq = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum == k:
            max_len = max(max_len, i+1)

        if curr_sum - k in freq:
            max_len = max(max_len, freq[curr_sum-k] + 1)
        
        freq[curr_sum-k] = i

    return max_len



if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1 ,1, 1]
    k = 3

    print(subArray(nums, k))
