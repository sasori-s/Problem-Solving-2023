def findProduct(A, n, left = 1, i = 0):
    if i == n:
        return 1
    
    curr = A[i]

    right = findProduct(A, n, left * A[i], i + 1)
    A[i] = left * right
    return curr * right

if __name__ == "__main__":
    A = [5 ,3, 4, 2, 6, 8]
    findProduct(A, len(A))
    print(A)