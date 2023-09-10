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

        swap(A, i, min)



if __name__ == '__main__':
    A = [3, 5, 8, 4, 1, 9, -2]

    selectionSort(A)
    print(A)