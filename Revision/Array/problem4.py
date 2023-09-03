def sort(A):
    k = 0

    for i in range(len(A)):
        if A[i] == 0:
            A[k] = 0
            k += 1

    for i in range(k, len(A)):
        A[k] = 1
        k += 1

if __name__ == '__main__':
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sort(A)
    print(A)