def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def partition(nums, start, end):
    pivot = nums[end]
    mid = start

    while mid <= end:
        if nums[mid] < pivot:
            swap(nums, start, mid)
            start += 1
            mid += 1

        elif nums[mid] > pivot:
            swap(nums, mid, end)
            end -= 1

        else:
            mid += 1

    return start - 1, mid

def quicksort(nums, start, end):
    if start >= end:
        return

    x, y = partition(nums, start, end)

    quicksort(nums, start, x)
    quicksort(nums, y, end)

if __name__ == "__main__":
    nums = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    quicksort(nums, 0, len(nums) - 1)
    print(nums)

