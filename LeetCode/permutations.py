def find(nums, result, index):
    if index == len(nums):
        result.append(nums[:])
        return

    for i in range(index, len(nums)):
        swap(i, index, nums)
        find(nums, result, index + 1)
        swap(i, index, nums)


def swap(i, j, A):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = []
    index = 0
    find(nums, result, index)
    print(result)
