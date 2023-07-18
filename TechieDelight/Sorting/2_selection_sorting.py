def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def selectionSort(A):
    for i in range(len(A) - 1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j

        if min != i:
            swap(A, i, min)

    # return A

if __name__ == "__main__":
    A = [4, 1, 9, 2, 3, 6]
    print(selectionSort(A))
    print(A)