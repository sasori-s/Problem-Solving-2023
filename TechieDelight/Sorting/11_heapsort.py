def LEFT(i):
    return 2 * i + 1

def RIGHT(i):
    return 2 * i + 2

def heapify(A, i, size):
    largest = i
    left = LEFT(i)
    right = RIGHT(i)

    if left < size and A[left] > A[largest]:
        largest = left

    if right < size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, size)

def pop(A, size):
    if size <= 0:
        return -1
    
    top = A[0]
    A[0] = A[size - 1]

    heapify(A, 0, size - 1)
    return top

def heapsort(A):
    n = len(A)
    i = (n - 2) // 2

    while i >= 0:
        heapify(A, i , n)
        i -= 1

    while n:
        A[n - 1] = pop(A, n)
        n -= 1


if __name__ == "__main__":
    A = [6, 4, 7, 1, 9, -2]
    heapsort(A)
    print(A)