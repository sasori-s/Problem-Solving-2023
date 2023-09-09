def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, low, high):
    pivot = A[high]

    pIndex = low

    for i in range(low, high):
        if A[i] <= pivot:
            swap(A, i, pIndex)
            pIndex += 1
        
    swap(A, high, pIndex)
    return pIndex

def quickSort(A, low, high):
    if low >= high:
        return 

    pivot = partition(A, low, high)
    quickSort(A, low, pivot - 1)
    quickSort(A, pivot + 1, high)



if __name__ == '__main__':
    A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    quickSort(A, 0, len(A) - 1)
    print(A)