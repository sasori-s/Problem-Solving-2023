def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A):
    pIndex = 0

    for i in range(len(A)):
        if A[i] < 0:
            swap(A, i, pIndex)
            pIndex += 1

if __name__ == '__main__':
    A = [ 9, -3, 5, -2, -8, -6, 1, 3]
    partition(A)

    print(A)