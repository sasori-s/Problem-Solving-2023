def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = []

    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i] 
            i += 1

        else:
            B[k] = A[j]
            j += 1

        k += 1

        if i > mid:
            while j <= right:
                B[k] = A[j]
                k += 1
                j += 1
        
        else:
            while i <= mid:
                B[k] = A[i]
                i += 1
                k += 1

        for k in range(len(A)):
            A[k] = B[k]

        return A
        

def mergeSort(A, left, right):
    if left < right:
        mid = (left + right) / 2
        mergeSort(A, left, mid)
        mergeSort(A, mid + 1, right)
        merge(A, left, mid, right)

if __name__ == "__main__":
    A = [9, 4, 7, 6, 3, 1, 5]
    print(mergeSort(A, 0, len(A) - 1))
