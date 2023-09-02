def binarySearch(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == A[mid]:
            return mid

        if target > A[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return None

if __name__ == '__main__':
    A = [2, 5, 6, 8, 9, 10]
    target = 5

    index = binarySearch(A, target)

    if index:
        print(f"{target} found at index {index}")
    else:
        print("{target} not found")