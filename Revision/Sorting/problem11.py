def LEFT(i):
    return 2*i + 1


def RIGHT(i):
    return 2*i + 2


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def pop(A, size):
    if size <= 0:
        return -1

    top = A[0]

    A[0] = A[size - 1]

    heapify(A, 0, size - 1)

    return top


def heapify(A, i, size):
    left = LEFT(i)
    right = RIGHT(i)

    largest = i

    if left < size and A[left] > A[i]:
        largest = left

    if right < size and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap(A, i, largest)
        heapify(A, largest, size)


def heapSort(A):
    n = len(A)
    i = (n - 2) // 2

    while i >= 0:
        heapify(A, i, n)
        i = i - 1

    while n:
        A[n - 1] = pop(A, n)
        n = n - 1


if __name__ == '__main__':
    A = [6, 4, 7, 1, 9, -2]
    heapSort(A)
    print(A)