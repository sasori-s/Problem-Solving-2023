# Print all subarrays with 0 sum
# Google Translate Icon
# Given an integer array, print all subarrays with zero-sum.

# For example,

# Input:  { 4, 2, -3, -1, 0, 4 }
 
# Subarrays with zero-sum are
 
# { -3, -1, 0, 4 }
# { 0 }
 
 
# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
# Subarrays with zero-sum are
 
# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }


def insert(d, key, value):
    d.setdefault(key, []).append(value)

def printallSublists(nums):
    d = {}
    insert(d, 0, -1)

    total = 0

    for i in range(len(nums)):
        total += nums[i]

        if total in d:
            list = d.get(total)

            for value in list:
                print("The sublist is ", (value + 1, i))
        
        insert(d, total, i)

if __name__ == "__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
 
    printallSublists(nums)