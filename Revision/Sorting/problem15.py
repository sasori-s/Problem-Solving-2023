def merge(A, aux, start, mid, end):
    k = i = start
    j = mid + 1
    inversionCOunt = 0

    while i <= mid and j <= end:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i += 1

        else:
            aux[k] = A[j]
            j += 1
            inversionCOunt += mid - i + 1

        k += 1

    while i <= mid:
        aux[k] = A[i]
        i += 1
        k += 1

    for i in range(start, end + 1):
        A[i] = aux[i]

    return inversionCOunt

def mergeSort(A, aux, start, end):
    if start >= end:
        return 0

    mid = start + ((end - start) >> 1)
    inversionCount = 0

    inversionCount += mergeSort(A, aux, start, mid)
    inversionCount += mergeSort(A, aux,  mid + 1, end)
    inversionCount += merge(A, aux, start, mid, end)


    return inversionCount


if __name__ == '__main__':
    A = [1, 9, 6, 4 , 5]
    aux = A.copy()
    
    print("The inversion count of the array is: ", mergeSort(A, aux, 0, len(A) - 1))