def merge(A, aux, low, mid, high, count):
    i = k = low
    j = mid + 1
    c = 0

    while i <= mid and j <= high:
        if A[i] > A[j]:
            count[A[i]] = count.get(A[i], 0) + c
            aux[k] = A[i]
            i += 1

        else:
            aux[k] = A[j]
            c += 1
            j += 1

        k += 1

    while i <= mid:
        count[A[i]] = count.get(A[i], 0) + c
        aux[k] = A[i]
        k = k + 1
        i += 1

    for i in range(low, high + 1):
        A[i] = aux[i]



def mergeSort(A, aux, low, high, count):
    if high <= low:
        return 

    mid = low + ((high - low) >> 1)

    mergeSort(A, aux, low, mid, count)
    mergeSort(A, aux, mid + 1, high, count)
    merge(A, aux, low, mid, high, count)

def getSurpasserCount(A):
    count = {}

    aux = A.copy()
    A = A.copy()

    mergeSort(A, aux, 0, len(A) - 1, count)
    return count


if __name__ == "__main__":
    A = [4, 6, 3, 9, 7, 10]
    surpasserCount = getSurpasserCount(A)

    for value in A:
        print(surpasserCount.get(value), end=" ")