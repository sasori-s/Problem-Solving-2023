def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, start, end):
    pivot = A[start]
    (i, j) = (start - 1, end + 1)

    while True:
        while True:
            i += 1
            if A[i] >= pivot:
                break

        while True:
            j -= 1
            if A[j] <= pivot:
                break

        if i >= j:
            return j

        swap(A, i, j)


def quickSort(A, start, end):
    if start >= end:
        return

    pivot = partition(A, start, end)
    quickSort(A, start, pivot)
    quickSort(A, pivot + 1, end)


A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
quickSort(A, 0, len(A) - 1)
print(A)