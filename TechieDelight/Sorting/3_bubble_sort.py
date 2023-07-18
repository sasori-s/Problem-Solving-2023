def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def bubbleSort(A):
    for i in range(len(A)):
        swapped = False

        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                swapped = True
                swap(A, j + 1, j)

        if not swapped:
            return A
            break
    # print(A)

if __name__ == "__main__":
    A = [4, 3, 7, 1, 5]
    print(bubbleSort(A))