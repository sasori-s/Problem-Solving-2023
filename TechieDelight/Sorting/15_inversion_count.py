def merge(A, aux, low, mid, high):
    i = k = low
    j = mid + 1
    inversionCount = 0

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        
        else:
            aux[k] = A[j]
            j = j + 1
            inversionCount += (mid - i + 1)
        
        k = k + 1

    while i <= mid:
        aux[k] = A[i]
        i += 1
        k += 1

    for i in range(low, high + 1):
        A[i] = aux[i]

    return inversionCount

def mergesort(A, aux, low, high):
    if low >= high:
        return 0

    mid = low + ((high - low) >> 1)
    inversionCount = 0

    inversionCount += mergesort(A, aux, low, mid)
    inversionCount += mergesort(A, aux, mid + 1, high)
    inversionCount += merge(A, aux, low, mid, high)

    return inversionCount


if __name__ == "__main__":
    A = [1, 9, 6, 4, 5]
    aux = A.copy()
    print(f"Inversion count is {mergesort(A, aux, 0, len(A)-1)}")
