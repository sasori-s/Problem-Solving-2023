def reorder(A):
    k = 0

    for i in A:
        if i:
            A[k] = i
            k = k + 1

    for i in range(k, len(A)):
        A[i] = 0

if __name__ == "__main__":
    A = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    reorder(A)
    print(A)