def insertionSort(A, i, n):
    value = A[i]
    j = i

    while j > 0 and A[j-1] > value:
        A[j] = A[j-1] 
        j = j - 1

    A[j] = value

    if i + 1 <= n:
        insertionSort(A, i+1, n)


if __name__ == "__main__":
    A = [3, 8, 5, 4, 1, 9, -2]
    insertionSort(A, 1, len(A) - 1)

    print(A)