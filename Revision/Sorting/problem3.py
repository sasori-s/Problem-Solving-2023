def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def bubbleSort(A):
    for i in range(len(A) - 1):
        swapped = False

        for j in range(len(A) - i - 1):
            if A[j + 1] < A[j]:
                swap(A, j, j + 1)
                swapped = True
        
        if not swapped:
            break

if __name__ == '__main__':
    A = [3, 5, 8, 4, 1, 9, -2]
    bubbleSort(A)
    print(A)