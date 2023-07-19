def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, start, end):
    pivot = A[end]
    pIndex = start

    for i in range(start, end):
        if A[i] <= pivot:
            swap(A, i, pIndex)
            pIndex += 1

    swap(A, end, pIndex)

    return pIndex


def quickSort(A, start, end):
    if start >= end:
        return

    pivot = partition(A, start, end)

    quickSort(A, start, pivot - 1)
    quickSort(A, pivot + 1, end)


if __name__ == '__main__':
    A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    quickSort(A, 0, len(A) - 1)
    print(A)

    