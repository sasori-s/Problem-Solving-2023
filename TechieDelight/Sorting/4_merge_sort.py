def merge(A, aux, low, mid, high):
    k = low
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i += 1
            k += 1

        else:
            aux[k] = A[j]
            j += 1
            k += 1
        
    while i <= mid:
        aux[k] = A[i]
        k += 1
        i += 1

        
    for i in range(low, high + 1):
        A[i] = aux[i]


def mergeSort(A, aux, low, high):
    if high <= low:
        return

    mid = (low + ((high - low) >> 1))

    mergeSort(A, aux, low, mid)
    mergeSort(A, aux, mid+1, high)
    merge(A, aux, low, mid, high)

def isSorted(A):
    prev = A[0]

    for i in range(1, len(A)):
        if prev > A[i]:
            print("The merge sort did not work")
            return False

        prev = A[i]

    return True


if __name__ == '__main__':
 
    A = [12, 3, 18, 24, 0, 5, -2]
    aux = A.copy()
 
    # sort list `A` using auxiliary list `aux`
    mergeSort(A, aux, 0, len(A) - 1)
 
    if isSorted(A):
        print(A)