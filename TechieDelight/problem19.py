def findProduct(A):
    n = len(A)
    left = [None] * n
    right = [None] * n

    if n == 0:
        return

    left[0] = 1

    for i in range(1, len(A)):
        left[i] = A[i - 1] * left[i - 1]

    right[n - 1] = 1

    for j in reversed(range(n - 1)):
        right[j] = right[j + 1] * A[j + 1]

    for i in range(n):
        A[i] = left[i] * right[i]
        
         

if __name__ == "__main__":
    A = [5, 3, 4, 2, 6, 8]
    findProduct(A)
    print(A)