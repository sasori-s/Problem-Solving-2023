def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, low, high):
    pivot = A[low]
    (i, j) = (low - 1, high + 1)

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


def quickSort(A, low, high):
    if low >= high:
        return

    pivot = partition(A, low, high)

    quickSort(A, low, pivot)
    quickSort(A, pivot + 1, high)

if __name__ == "__main__":
    A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    quickSort(A, 0, len(A) - 1)
    print(A)