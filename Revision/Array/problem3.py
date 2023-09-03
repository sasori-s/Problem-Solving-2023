def insert(d, key, value):
    d.setdefault(key, []).append(value)

def printAllSublists(nums):
    d = {}
    insert(d, 0, -1)

    total = 0

    for i in range(len(nums)):
        total += nums[i]

        if total in d:
            list = d.get(total)

            for index in list:
                print("Pair found at ", (index + 1, i))

        insert(d, total, i)



if __name__ == "__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

    printAllSublists(nums)