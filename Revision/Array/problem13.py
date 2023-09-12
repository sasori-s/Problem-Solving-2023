def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def rearrangeArray(A):
    for i in range(1, len(A), 2):
        if A[i - 1] > A[i]:
            swap(A, i - 1, i)

        if i + 1 < len(A) and A[i + 1] > A[i]:
            swap(A, i + 1, i)

if __name__ == '__main__':
    A = [9, 6, 8, 3, 7]

    rearrangeArray(A)
    print(A)