def merge(A, aux, low, mid, high):
    i = k = low
    j = mid + 1

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i += 1

        else:
            aux[k] = A[j]
            j += 1

        k += 1

    while i <= mid:
        aux[k] = A[i]
        i += 1
        k += 1

    for i in range(low, high + 1):
        A[i] = aux[i]

def mergeSort(A, aux, low, high):
    if high <= low:
        return

    mid = (low + ((high - low) >> 1))

    mergeSort(A, aux, low, mid)
    mergeSort(A, aux, mid + 1, high)

    merge(A, aux, low, mid, high)

if __name__ == '__main__':
    A = [12, 3, 18, 24, 0, 5, -2]
    aux = A.copy()

    mergeSort(A, aux, 0, len(A) - 1)
    print(A)