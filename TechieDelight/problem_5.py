# Find maximum length subarray having a given sum
# Google Translate Icon
# Given an integer array, find the maximum length subarray having a given sum.

# For example, consider the following array:

# nums[] = { 5, 6, -5, 5, 3, 5, 3, -2, 0 }
# target = 8
 
 
# Subarrays with sum 8 are
 
# { -5, 5, 3, 5 }
# { 3, 5 }
# { 5, 3 }
 
# The longest subarray is { -5, 5, 3, 5 } having length 4


def findMaxLenSublist(nums, target):
    d = {}
    d[0]= -1
    length = 0
    total = 0
    ending_index = -1

    for i in range(len(nums)):
        total += nums[i]

        if total not in d:
            d[total] = i
        
        if total - target in d and length < i - d[total - target]:
            length = i - d[total - target]
            ending_index = i

    print((ending_index - length + 1, ending_index))




if __name__ == '__main__':
    nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    target = 8
 
    findMaxLenSublist(nums, target)