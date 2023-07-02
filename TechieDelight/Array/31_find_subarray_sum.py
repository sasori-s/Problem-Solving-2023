def findSublists(nums, target):
    s = set()
    s.add(0)

    sum_so_far = 0
    
    for i in nums:
        sum_so_far += i

        if (sum_so_far - target) in s:
            return True
        
        s.add(sum_so_far)

    return False
            

if __name__ == "__main__":
    nums = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    target = -3

    if findSublists(nums, target):
        print("Sublist with the given sum exists")
    else:
        print("Sublist with the given sum does not exist")