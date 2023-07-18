def merge(A, temp, frm, mid, to):
    i = frm
    k = frm
    j = mid + 1

    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i += 1
        
        else:
            temp[k] = A[j]
            j += 1

        k += 1

    while i < len(A) and i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1

    for i in range(frm, to + 1):
        A[i] = temp[i]

def mergeSort(A):
    low = 0
    high = len(A) - 1

    temp = A.copy()
    m = 1

    while m <= high -  low :
        for i in range(low, high, 2*m):
            frm = i
            mid = i + m - 1
            to = min(i + 2*m - 1, high)

            merge(A, temp, frm, mid, to)

        m = 2 *m

if __name__ == '__main__':
 
    A = [5, 7, -9, 3, -4, 2, 8]
 
    print("Original array:", A)
    mergeSort(A)
    print("Modified array:", A)