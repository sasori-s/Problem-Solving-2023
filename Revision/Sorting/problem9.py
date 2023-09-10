def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A ,start, end):
    mid = start
    pivot = A[end]

    while mid <= end:
        if A[mid] < pivot:
            swap(A, start, mid)
            mid += 1
            start += 1

        elif A[mid] > pivot:
            swap(A, mid, end)
            end -= 1

        else:
            mid += 1

    return start - 1, mid

def quickSort(A, start, end):
    if start >= end:
        return

    x, y = partition(A, start, end)
    quickSort(A, start, x)
    quickSort(A, y, end)

if __name__ == '__main__':
    A = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    quickSort(A, 0, len(A) - 1)
    print(A)